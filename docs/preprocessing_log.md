# Preprocessing and Feature Engineering Decision Log

**Lead Engineer:** H A Wickramathilaka (IT24100427) — AI Specialization  
**Assigned Task:** Data Cleaning, Feature Construction, Encoding, Scaling, and Leakage Prevention  
**Group ID:** 2026-AI-07  
**Module:** IT3091 Machine Learning Project  
**Primary Artifact:** [`notebooks/02_preprocessing_and_feature_engineering.ipynb`](../notebooks/02_preprocessing_and_feature_engineering.ipynb)  

---

### 1. Missing Value and Whitespace Remediation (DEC-03)
* **Observed Anomaly:** The `TotalCharges` variable contains 11 whitespace records (`" "`) causing Pandas to infer an `object` data type.
* **Visual Evidence:** Section 1 bar plot proves 100% of blank records have `tenure = 0`.
* **Options Considered:**
  1. *Row Deletion:* Drop all 11 records.
  2. *Central Tendency Imputation:* Replace with mean or median `TotalCharges`.
  3. *Structural Domain Imputation:* Replace with `0.0`.
* **Decision Chosen:** Option 3 (`TotalCharges = 0.0`).
* **Justification:** Every instance with whitespace has `tenure = 0`. These are newly activated subscribers who have not completed their first billing cycle. Deleting them biases the dataset by removing new customers, while mean imputation inflates their historical spend. Imputing `0.0` reflects actual financial billing reality.

---

### 2. Domain-Specific Feature Engineering (DEC-04)
* **Visual Validation (Notebook Section 2):**
  * `IsAutomaticPayment`: Binary feature isolating automated vs. manual billing. Visualized in Section 2: Manual billing users churn at **37.6%** vs. **15.9%** for automated users (2.4x reduction in attrition risk).
  * `ServiceBundleCount`: Integer count capturing total subscribed value-added services (`OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`). Visualized in Section 2: Churn rate drops monotonically from **42.2%** for 0 add-ons down to **8.6%** for 5 add-ons, proving cumulative platform stickiness.
  * `TenureCohort`: Binned customer lifecycle stages (`Cohort_0_12m`, `Cohort_13_24m`, `Cohort_25_48m`, `Cohort_49_72m`). Section 2 confirms churn peaks at **47.7%** in months 0–12 and plunges to **6.6%** past 48 months.

---

### 3. Leakage Prevention Protocol (DEC-05)
* **Protocol:** Data is partitioned into training (80%) and testing (20%) sets using `stratify=y` prior to any feature transformation.
* **Visual Integrity Check (Notebook Section 3):** Preserves an identical **26.54% churn rate** across both `X_train` and `X_test`.
* **Justification:** Fitting scalers or encoders on the entire dataset leaks global summary statistics ($\mu, \sigma$) from the holdout test set into training, resulting in overly optimistic evaluation metrics. The `ColumnTransformer` is strictly fit on `X_train` and applied down to `X_test`.

---

### 4. Feature Transformations & Scaling (DEC-05)
* **Categorical Features:** Encoded using `OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')` to prevent dummy variable traps while maintaining linear independence for baseline models.
* **Continuous Features:** Standardized using `StandardScaler` to ensure zero mean ($\mu \approx 0.0$) and unit variance ($\sigma \approx 1.0$).
* **Visual Audit (Notebook Section 4):** Before-vs-After KDE curves verify successful variance alignment across `tenure`, `MonthlyCharges`, `TotalCharges`, and `ServiceBundleCount`.

---

### 5. Class Imbalance Strategy (DEC-06)
* **Observed Imbalance:** 73.46% negative class (`No Churn`) vs. 26.54% positive class (`Churn`).
* **Decision Chosen:** Preserve the real-world operational class distribution in test splits and apply algorithmic cost weighting (`class_weight='balanced'` in Logistic Regression and Random Forest; `scale_pos_weight` in XGBoost).
* **Justification:** Synthetic oversampling (such as SMOTE) creates artificial feature interpolations in sparse categorical spaces, distorting probability calibration. Cost-sensitive weighting penalizes minority errors without compromising empirical data fidelity.
