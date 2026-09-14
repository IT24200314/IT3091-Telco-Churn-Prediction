# Preprocessing and Feature Engineering Decision Log

**Lead Engineer:** H A Wickramathilaka (IT24100427) — AI Specialization  
**Assigned Task:** Data Cleaning, Feature Construction, Encoding, Scaling, and Leakage Prevention  
**Group ID:** 2026-AI-07  
**Module:** IT3091 Machine Learning Project  

---

### 1. Missing Value and Whitespace Remediation
* **Observed Anomaly:** The `TotalCharges` variable contains 11 whitespace records (`" "`) causing Pandas to infer an `object` data type.
* **Options Considered:**
  1. *Row Deletion:* Drop all 11 records.
  2. *Central Tendency Imputation:* Replace with mean or median `TotalCharges`.
  3. *Structural Domain Imputation:* Replace with `0.0`.
* **Decision Chosen:** Option 3 (`TotalCharges = 0.0`).
* **Justification:** Every instance with whitespace has `tenure = 0`. These are newly activated subscribers who have not completed their first billing cycle. Deleting them biases the dataset by removing new customers, while mean imputation inflates their historical spend. Imputing `0.0` reflects actual financial billing reality.

---

### 2. Leakage Prevention Protocol
* **Protocol:** Data is split into training (80%) and testing (20%) sets using `stratify=y` prior to any feature transformation.
* **Justification:** Fitting scalers or encoders on the entire dataset leaks global summary statistics ($\mu, \sigma$) from the holdout test set into training, resulting in overly optimistic evaluation metrics. The `ColumnTransformer` is strictly fit on `X_train` and applied down to `X_test`.

---

### 3. Feature Transformations
* **Categorical Features:** Encoded using `OneHotEncoder(drop='first', sparse_output=False)` to prevent dummy variable traps while maintaining linear independence for baseline models.
* **Continuous Features:** Standardized using `StandardScaler` to ensure zero mean and unit variance ($\mu = 0, \sigma = 1$), preventing features with larger nominal scales (`TotalCharges`) from dominating gradient updates.
* **Engineered Features:**
  * `ServiceBundleCount`: Integer count capturing total subscribed services. Hypothesized that higher service adoption increases platform stickiness and switching costs.
  * `IsAutomaticPayment`: Binary feature isolating automated vs. manual billing methods.
  * `TenureCohort`: Binned representation to capture non-linear retention dynamics across customer lifecycles.

---

### 4. Class Imbalance Strategy
* **Observed Imbalance:** 73.46% negative class (`No Churn`) vs. 26.54% positive class (`Churn`).
* **Decision Chosen:** Preserve the real-world operational class distribution in test splits and apply algorithmic cost weighting (`class_weight='balanced'` in Logistic Regression and Random Forest; `scale_pos_weight` in XGBoost).
* **Justification:** Synthetic oversampling (such as SMOTE) creates artificial feature interpolations in sparse categorical spaces, distorting probability calibration. Cost-sensitive weighting penalizes minority errors without compromising empirical data fidelity.
