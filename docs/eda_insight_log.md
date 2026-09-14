# Exploratory Data Analysis (EDA) Insight Log

**Lead Analyst:** E J M H D Bandara (IT24102278) — Data Science Specialization  
**Assigned Task:** Data Understanding, Statistical Profiling, and Data Quality Reasoning  
**Group ID:** 2026-AI-07  
**Module:** IT3091 Machine Learning Project  

---

### 1. Target Imbalance Analysis
* **Finding:** The target variable `Churn` is imbalanced, with **73.46% (5,174 subscribers)** staying and **26.54% (1,869 subscribers)** leaving.
* **ML Impact:** A naive baseline predicting all subscribers as "No Churn" yields 73.46% accuracy while failing to identify any at-risk customers. Evaluation must prioritize **Recall**, **Precision-Recall AUC (PR-AUC)**, and **ROC-AUC** rather than raw classification accuracy.

---

### 2. High-Risk Customer Segments
* **Contract Commitment:** Subscribers on `Month-to-month` contracts exhibit a **42.71% churn rate**, compared to **11.27%** for `One year` and **2.83%** for `Two year` contracts.
* **Internet Technology:** `Fiber optic` users have an attrition rate of **41.89%**, compared to **18.96%** for `DSL` and **7.40%** for users without internet service. This signals service instability or competitive pricing pressure in high-speed tiers.
* **Payment Channels:** Customers utilizing `Electronic check` experience a **45.29% churn rate**, while automated channels (`Bank transfer` and `Credit card`) maintain churn rates below **17%**. Manual payment workflows present regular friction points.
* **Customer Tenure (Tenure Cliff):** Churn heavily concentrates within the first **1 to 6 months** of onboarding. Subscribers surviving past 24 months show a steep drop in attrition probability.

---

### 3. Data Quality Issues & Anomaly Log
* **TotalCharges Whitespace Strings:** Exactly 11 rows in `TotalCharges` contain `' '` (a space character) instead of numeric digits.
  * *Root Cause Analysis:* All 11 instances have `tenure = 0`. These correspond to new subscribers who joined during the active billing cycle and have not yet completed a billing cycle.
  * *Remediation Strategy:* Rather than dropping rows (which causes data loss), impute `TotalCharges = 0.0` and cast the column to `float64`.
* **Multicollinearity:** `TotalCharges` demonstrates a high linear correlation with `tenure` ($r = 0.83$). Tree-based algorithms tolerate this correlation, but linear baseline models will require regularization (Ridge/Lasso penalties).
