# End-to-End Machine Learning Workflow Diagram

**Module:** IT3091 Machine Learning Project  
**Group ID:** 2026-AI-07  
**Lead Author:** D G N S Widumini (IT24101176) & U P M U I Ekanayake (IT24200314)  
**Rubric Criterion:** Workflow diagram and decision log (10 Marks)  
**Fink Alignment:** Integration; Learning How to Learn  

---

## 1. Visual Workflow Diagram

![IT3091 Machine Learning End-to-End Workflow Diagram](../reports/figures/00_workflow_diagram.png)

---

## 2. Interactive Architecture Pipeline (Mermaid)

```mermaid
flowchart TD
    subgraph S1["Stage 1: Business Problem Framing (Widumini)"]
        A1["Business Scenario: Guided Track (Code 7)<br/>Telco Customer Churn"] --> A2["Primary Lens: Churn Risk Prediction<br/>Secondary Lens: Retention Segment Analysis"]
        A2 --> A3["Cost Matrix Formulation<br/>Cost(FN)=$500 (Lost Customer)<br/>Cost(FP)=$50 (Retention Offer)"]
        A3 --> A4["Decision: Reject Naive Accuracy<br/>Target Metrics: Recall, PR-AUC, ROC-AUC<br/>(DEC-01, DEC-02)"]
    end

    subgraph S2["Stage 2: Data Understanding & Profiling (Bandara)"]
        B1["Raw Dataset Ingestion<br/>7,043 rows x 21 columns<br/>SHA256: 16320c9c..."] --> B2["Formal Data Dictionary<br/>21 Variables Cataloged"]
        B2 --> B3["Anomaly Audit: 11 Blank Spaces<br/>Proved tenure == 0 (New Subscribers)"]
        B3 --> B4["Discovery of 'Tenure Cliff'<br/>Peak Churn in Months 1-6<br/>(DEC-03)"]
    end

    subgraph S3["Stage 3: Preprocessing & Feature Engineering (Wickramathilaka)"]
        C1["Data Hygiene: Impute TotalCharges=0.0<br/>Cast to float64"] --> C2["Domain Feature Engineering<br/>• IsAutomaticPayment<br/>• ServiceBundleCount<br/>• TenureCohort<br/>(DEC-04)"]
        C2 --> C3["Leakage Prevention Protocol<br/>Stratified 80/20 Train-Test Split<br/>Strictly Fit ColumnTransformer on X_train<br/>(DEC-05)"]
        C3 --> C4["Transformations: StandardScaler + OneHotEncoder<br/>Preserve Empirical Class Distribution<br/>(DEC-06)"]
    end

    subgraph S4["Stage 4: Multi-Model Benchmark (Ekanayake)"]
        D1["Model Portfolio Setup<br/>Dummy, Logistic Regression, Random Forest,<br/>HistGradientBoosting, SVC"] --> D2["Stratified 5-Fold Cross-Validation<br/>Strictly on X_train (5,634 rows)<br/>(DEC-07)"]
        D2 --> D3["Benchmark Selection<br/>Champion: Logistic Regression (L2)<br/>CV ROC-AUC: 0.8463, CV Recall: 0.7960<br/>(DEC-08)"]
    end

    subgraph S5["Stage 5: Threshold Optimization & Diagnostics (Ekanayake)"]
        E1["Holdout Test Set Evaluation<br/>1,409 unseen accounts<br/>Test ROC-AUC: 0.8480"] --> E2["Cost-Sensitive Threshold Tuning<br/>Continuous Loss Curve Across [0.05, 0.95]<br/>Optimal Cutoff: tau* = 0.44<br/>(DEC-09)"]
        E2 --> E3["Financial Impact Calculation<br/>Net Savings: $19,250 over default 0.50<br/>Total Value: $152,300 over doing nothing"]
        E3 --> E4["Model Explainability (XAI)<br/>Log-Odds Coefficients Extraction<br/>Export to models/champion_model.joblib"]
    end

    subgraph S6["Stage 6: Operational Retention Playbook (Widumini)"]
        F1["3-Tier Customer Risk Routing<br/>• Tier 1 (High >= 0.65): Concierge Call<br/>• Tier 2 (Mod 0.40-0.65): $10 AutoPay Credit<br/>• Tier 3 (Low < 0.40): Loyalty Care"] --> F2["Responsible AI & Fairness Audit<br/>Verified Gender Disparity < 1.5%<br/>Senior Citizen Fixed-Income Safeguards"]
        F2 --> F3["Final Report & Video Demo<br/>Reproducible Codebase & AI Declaration"]
    end

    S1 --> S2
    S2 --> S3
    S3 --> S4
    S4 --> S5
    S5 --> S6
```

---

## 3. Workflow Decision Traceability Matrix

| Workflow Stage | Operational Owner | Core Deliverable Artifact | Architectural Decision Log Reference | Rubric Alignment |
| :--- | :--- | :--- | :--- | :--- |
| **1. Problem Framing** | D G N S Widumini | `docs/problem_framing.md` | **DEC-01** (Guided Track), **DEC-02** (Metric Choice) | Problem Framing (5m) |
| **2. Data Understanding** | E J M H D Bandara | `docs/data_dictionary.md`, `notebooks/01_eda_and_audit.ipynb` | **DEC-03** (Imputation of 11 blank records) | Data Understanding & EDA (10m) |
| **3. Preprocessing** | H A Wickramathilaka | `src/preprocessing.py`, `notebooks/02_preprocessing.ipynb` | **DEC-04** (Features), **DEC-05** (Leakage), **DEC-06** (Weights) | Preprocessing Decisions (15m) |
| **4. Modeling Strategy** | U P M U I Ekanayake | `src/train_and_evaluate.py`, `notebooks/03_model_training.ipynb` | **DEC-07** (5-Fold CV), **DEC-08** (Champion Selection) | Model Strategy (20m) |
| **5. Diagnostics & Tuning** | U P M U I Ekanayake | `reports/figures/08_threshold_cost_curve.png`, `models/` | **DEC-09** (Cost-Optimal Cutoff $\tau^* = 0.44$) | Evaluation & Judgement (20m) |
| **6. Business Action** | D G N S Widumini | `docs/business_recommendations.md`, `docs/final_report.md` | Master Final Report & Responsible AI Audit | Recommendations & Ethics (10m) |
