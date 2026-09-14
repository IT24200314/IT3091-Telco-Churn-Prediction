# Exploratory Data Analysis (EDA) Insight Log

**Lead Analyst:** E J M H D Bandara (IT24102278) — Data Science Specialization  
**Assigned Task:** Data Understanding, Statistical Profiling, and Data Quality Reasoning  
**Group ID:** 2026-AI-07  
**Module:** IT3091 Machine Learning Project  
**Primary Artifact:** [`notebooks/01_eda_and_audit.ipynb`](../notebooks/01_eda_and_audit.ipynb)  

---

### 1. Target Imbalance Analysis (Notebook Section 2)
* **Empirical Finding:** The target variable `Churn` is imbalanced, with **73.46% (5,174 subscribers)** staying and **26.54% (1,869 subscribers)** leaving (~2.77:1 ratio).
* **Visual Evidence:** Section 2 bar chart displays explicit subscriber volume and percentage annotations.
* **ML Modeling Impact (DEC-02):** A naive baseline predicting all subscribers as "No Churn" yields 73.46% accuracy while failing to identify a single at-risk customer. Evaluation must prioritize **Recall**, **Precision-Recall AUC (PR-AUC)**, and **ROC-AUC** rather than raw classification accuracy.

---

### 2. High-Risk Customer Segments & Business Drivers (Notebook Sections 3, 4, 5, 6)
* **The "Tenure Cliff" (Section 3):** Churn heavily concentrates within the first **1 to 6 months** of onboarding (median churned tenure = 10 months vs. 38 months for retained). Subscribers surviving past 24 months show a steep drop in attrition probability.
* **Price Sensitivity (Section 3):** Churners cluster at higher monthly bills ($70 - $105/month, median ~$79.65 vs. $64.43 for retained).
* **Contract Commitment (Section 4):** Subscribers on `Month-to-month` contracts exhibit a **42.71% churn rate**, compared to **11.27%** for `One year` and **2.83%** for `Two year` contracts.
* **Internet Technology (Section 4):** `Fiber optic` users have an attrition rate of **41.89%**, compared to **18.96%** for `DSL` and **7.40%** for users without internet service. This signals service instability or competitive pricing pressure in high-speed tiers.
* **Value-Added Service Retention Anchors (Section 5):** Customers subscribing to `TechSupport` (15.16% churn vs. 41.64% without) and `OnlineSecurity` (14.61% churn vs. 41.77% without) churn nearly **3x less**.
* **Payment Channels & Billing Friction (Section 6):** Customers utilizing `Electronic check` experience a **45.29% churn rate**, while automated channels (`Bank transfer` at 16.71% and `Credit card` at 15.24%) maintain stable tenure.

---

### 3. Data Quality Issues & Anomaly Log (Notebook Section 1)
* **TotalCharges Whitespace Strings:** Exactly 11 rows in `TotalCharges` contain `' '` (a space character) instead of numeric digits.
  * *Root Cause Analysis:* All 11 instances have `tenure = 0`. These correspond to new subscribers who joined during the active billing cycle and have not yet completed a billing cycle.
  * *Remediation Strategy (DEC-03):* Rather than dropping rows (which causes data loss and removes new accounts), impute `TotalCharges = 0.0` and cast the column to `float64`.
* **Multicollinearity (Section 7):** `TotalCharges` demonstrates a high linear correlation with `tenure` ($r = 0.83$). Tree-based algorithms tolerate this correlation, but linear baseline models will require regularization (Ridge/Lasso penalties).

---

### 4. Direct Preprocessing Handoff Matrix (To H A Wickramathilaka)

| Identified Data Pattern | Visual Proof in Notebook | Preprocessing Decision | Architectural Reference |
| :--- | :--- | :--- | :--- |
| 11 blank spaces in `TotalCharges` | Section 1 Schema Audit | Impute `0.0` (all have `tenure = 0`) & cast to `float64` | **DEC-03** |
| Target imbalance (73.5% / 26.5%) | Section 2 Distribution Bar | Stratified train/test splitting & algorithmic cost weighting | **DEC-02** |
| 0-12m Tenure Cliff | Section 3 KDE & Boxplot | Feature engineering: `TenureCohort` categorical bins | **DEC-04** |
| 3x Retention from Add-on Services | Section 5 Multi-bar Comparison | Feature engineering: `ServiceBundleCount` integer count | **DEC-04** |
| Electronic Check Friction (45.3%) | Section 6 Payment Channel Bar | Feature engineering: `IsAutomaticPayment` binary flag | **DEC-04** |
| $r = 0.83$ collinearity | Section 7 Correlation Heatmap | Continuous variable normalization via `StandardScaler` | **DEC-05** |
