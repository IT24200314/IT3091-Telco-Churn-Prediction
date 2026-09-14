import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, roc_curve, precision_recall_curve,
    confusion_matrix
)

# Visual configuration
sns.set_theme(style="whitegrid")
plt.rcParams.update({"font.sans-serif": "Arial", "font.size": 10})
os.makedirs("reports/figures", exist_ok=True)
os.makedirs("models", exist_ok=True)

# 1. Load Processed Datasets
X_train = pd.read_csv("data/processed/X_train.csv")
y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()
X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv").values.ravel()

print(f"Loaded Training Data: {X_train.shape}, Test Data: {X_test.shape}")

# 2. Define Model Portfolio
models = {
    "Dummy (Naive Baseline)": DummyClassifier(strategy="most_frequent"),
    "Logistic Regression (Baseline)": LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=150, max_depth=10, class_weight="balanced_subsample", random_state=42),
    "HistGradientBoosting": HistGradientBoostingClassifier(max_iter=150, random_state=42),
    "Support Vector Classifier (RBF)": SVC(kernel="rbf", class_weight="balanced", probability=True, random_state=42)
}

# 3. Stratified 5-Fold Cross-Validation Benchmark
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scoring = ["accuracy", "recall", "precision", "f1", "roc_auc", "average_precision"]

cv_results = []
print("\n--- Running Stratified 5-Fold Cross-Validation ---")
for name, model in models.items():
    scores = cross_validate(model, X_train, y_train, cv=cv, scoring=scoring, n_jobs=-1)
    cv_results.append({
        "Model": name,
        "CV_ROC_AUC": scores["test_roc_auc"].mean(),
        "CV_PR_AUC": scores["test_average_precision"].mean(),
        "CV_Recall": scores["test_recall"].mean(),
        "CV_Precision": scores["test_precision"].mean(),
        "CV_F1": scores["test_f1"].mean(),
        "CV_Accuracy": scores["test_accuracy"].mean()
    })
    print(f"Completed: {name}")

cv_df = pd.DataFrame(cv_results)
cv_df.to_csv("reports/cv_model_comparison.csv", index=False)
print("\nCross-Validation Summary:")
print(cv_df.round(4).to_string(index=False))

# --- Figure 1: 5-Fold CV Model Comparison Bar Plot ---
fig, ax = plt.subplots(figsize=(10, 5))
tidy_cv = cv_df[cv_df["Model"] != "Dummy (Naive Baseline)"].melt(
    id_vars="Model", value_vars=["CV_ROC_AUC", "CV_PR_AUC", "CV_Recall", "CV_F1"],
    var_name="Metric", value_name="Score"
)
sns.barplot(data=tidy_cv, x="Model", y="Score", hue="Metric", palette="Blues_r", ax=ax)
ax.set_title("5-Fold Stratified Cross-Validation Benchmark (Holdout Train Set)", weight="bold", fontsize=12)
ax.set_ylim(0.4, 0.9)
ax.set_ylabel("Validation Score")
plt.xticks(rotation=15)
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig("reports/figures/06_cv_model_comparison.png", dpi=300)
plt.close()

# 4. Holdout Test Set Evaluation & ROC / PR Curves
trained_models = {}
test_preds = {}
test_probs = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    trained_models[name] = model
    test_preds[name] = model.predict(X_test)
    if hasattr(model, "predict_proba"):
        test_probs[name] = model.predict_proba(X_test)[:, 1]
    else:
        test_probs[name] = np.zeros(len(y_test))

# --- Figure 2: ROC Curves & PR Curves ---
fig, (ax_roc, ax_pr) = plt.subplots(1, 2, figsize=(14, 6))

colors = {"Dummy (Naive Baseline)": "gray", "Logistic Regression (Baseline)": "#1f77b4",
          "Random Forest": "#2ca02c", "HistGradientBoosting": "#ff7f0e", "Support Vector Classifier (RBF)": "#d62728"}

for name in models.keys():
    if name == "Dummy (Naive Baseline)":
        continue
    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, test_probs[name])
    auc_val = roc_auc_score(y_test, test_probs[name])
    ax_roc.plot(fpr, tpr, label=f"{name} (AUC = {auc_val:.3f})", color=colors[name], linewidth=2)
    
    # PR Curve
    prec, rec, _ = precision_recall_curve(y_test, test_probs[name])
    pr_auc_val = average_precision_score(y_test, test_probs[name])
    ax_pr.plot(rec, prec, label=f"{name} (PR-AUC = {pr_auc_val:.3f})", color=colors[name], linewidth=2)

ax_roc.plot([0, 1], [0, 1], "k--", alpha=0.6)
ax_roc.set_title("Receiver Operating Characteristic (ROC) Curves", weight="bold")
ax_roc.set_xlabel("False Positive Rate")
ax_roc.set_ylabel("True Positive Rate (Recall)")
ax_roc.legend(loc="lower right")

ax_pr.set_title("Precision-Recall (PR) Curves", weight="bold")
ax_pr.set_xlabel("Recall")
ax_pr.set_ylabel("Precision")
ax_pr.legend(loc="lower left")

plt.tight_layout()
plt.savefig("reports/figures/07_roc_and_pr_curves.png", dpi=300)
plt.close()

# 5. Cost-Sensitive Threshold Optimization (For Logistic Regression & HistGradientBoosting)
# Cost Assumptions: False Negative (Lost customer) = $500; False Positive (Retention incentive) = $50
cost_fn = 500
cost_fp = 50

best_model_name = "Logistic Regression (Baseline)"
probs_best = test_probs[best_model_name]

thresholds = np.linspace(0.1, 0.9, 81)
cost_curve = []

for th in thresholds:
    binary_preds = (probs_best >= th).astype(int)
    cm = confusion_matrix(y_test, binary_preds)
    # cm: [[TN, FP], [FN, TP]]
    fp = cm[0, 1]
    fn = cm[1, 0]
    total_cost = (fn * cost_fn) + (fp * cost_fp)
    cost_curve.append({
        "Threshold": th,
        "Total_Cost": total_cost,
        "False_Negatives": fn,
        "False_Positives": fp,
        "Recall": recall_score(y_test, binary_preds),
        "Precision": precision_score(y_test, binary_preds, zero_division=0)
    })

cost_df = pd.DataFrame(cost_curve)
optimal_idx = cost_df["Total_Cost"].idxmin()
opt_threshold = cost_df.loc[optimal_idx, "Threshold"]
min_cost = cost_df.loc[optimal_idx, "Total_Cost"]
default_cost = cost_df[cost_df["Threshold"].round(2) == 0.50]["Total_Cost"].values[0]

print(f"\nDefault Threshold (0.50) Business Cost: ${default_cost:,.2f}")
print(f"Optimal Threshold ({opt_threshold:.2f}) Business Cost: ${min_cost:,.2f}")
print(f"Cost Savings via Threshold Optimization: ${default_cost - min_cost:,.2f}")

# --- Figure 3: Cost-Sensitive Threshold Curve ---
fig, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(cost_df["Threshold"], cost_df["Total_Cost"], color="#b2182b", linewidth=2.5, label="Total Business Cost ($)")
ax1.axvline(0.50, color="gray", linestyle="--", label="Default Threshold (0.50)")
ax1.axvline(opt_threshold, color="#2166ac", linestyle="-.", label=f"Cost-Optimal Threshold ({opt_threshold:.2f})")
ax1.set_xlabel("Classification Probability Cutoff Threshold")
ax1.set_ylabel("Total Business Cost ($)", color="#b2182b")
ax1.set_title("Operational Cost vs. Decision Threshold Curve", weight="bold")
ax1.legend(loc="upper center")
plt.tight_layout()
plt.savefig("reports/figures/08_threshold_cost_curve.png", dpi=300)
plt.close()

# --- Figure 4: Feature Importance / Attribution ---
lr_model = trained_models["Logistic Regression (Baseline)"]
coef_df = pd.DataFrame({
    "Feature": X_train.columns,
    "Coefficient": lr_model.coef_[0]
}).sort_values(by="Coefficient", key=abs, ascending=False).head(12)

plt.figure(figsize=(9, 5))
colors_coef = ["#d95f02" if x > 0 else "#2b5c8f" for x in coef_df["Coefficient"]]
sns.barplot(data=coef_df, x="Coefficient", y="Feature", hue="Feature", palette=colors_coef, legend=False)
plt.title("Top 12 Churn Drivers (Logistic Regression Log-Odds Coefficients)", weight="bold")
plt.xlabel("Log-Odds Impact (Positive = Increases Churn Risk, Negative = Protects Retention)")
plt.tight_layout()
plt.savefig("reports/figures/09_feature_importances.png", dpi=300)
plt.close()

# 6. Save Trained Model Artifacts to models/
import joblib
best_model = trained_models["Logistic Regression (Baseline)"]
joblib.dump(best_model, "models/champion_logistic_regression.joblib")
joblib.dump(best_model, "models/champion_model.joblib")
joblib.dump(trained_models, "models/all_trained_models.joblib")
print("[SUCCESS] Champion model exported to models/champion_logistic_regression.joblib and models/champion_model.joblib")

print("\nPhase 3 execution complete. Visual figures saved in reports/figures/ and models saved in models/.")

