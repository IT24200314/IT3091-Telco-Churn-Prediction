# Individual A4 Personal Learning Journey Report

**Student Name:** H A Wickramathilaka  
**Student ID:** IT24100427  
**Degree Specialization:** B.Sc. (Hons) in Information Technology — Artificial Intelligence  
**Group ID:** 2026-AI-07  
**Module:** IT3091 Machine Learning Project  
**Assigned Role:** Preprocessing & Feature Engineering Pipeline Lead  

---

### 1. Specific Technical Contributions & Ownership
* **Leakage-Proof Pipeline Architecture:** Engineered the modular data preprocessing pipeline (`src/preprocessing.py`) utilizing scikit-learn's `ColumnTransformer` to enforce strict train/test separation before fitting scalers and encoders.
* **Interactive Preprocessing Notebook:** Developed and executed `notebooks/02_preprocessing_and_feature_engineering.ipynb`, providing visual verification of zero data leakage, before/after scaling density distributions, and feature correlations.
* **Domain Feature Engineering:** Formulated and implemented three impactful behavioral features: `IsAutomaticPayment` (binary flag), `ServiceBundleCount` (discrete integer count), and `TenureCohort` (categorical lifecycle bins).
* **Pipeline Artifact Export:** Exported the transformed feature matrices (`X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`) to `data/processed/` and serialized the fitted pipeline to `models/preprocessor.joblib`.

---

### 2. Key Technical Hurdle Overcome
* **The Problem:** Data leakage represents one of the most pervasive failure modes in machine learning. Fitting standard scalers or one-hot encoders across the entire dataset inadvertently contaminates the training folds with global distributional statistics ($\mu, \sigma$) from the holdout evaluation set, inflating validation metrics.
* **The Solution:** Implemented a rigorous leakage-prevention protocol (**DEC-05**). An 80/20 stratified split (`stratify=y, random_state=42`) was executed *prior* to instantiating any transformation steps. The `ColumnTransformer` was fitted strictly on `X_train` and then applied to `X_test` via `.transform()`, with visual split checks confirming identical 26.54% churn prevalence across both subsets.

---

### 3. Fink's Taxonomy of Significant Learning Alignment
* **Foundational Knowledge:** Deepened theoretical understanding of feature scaling dynamics (Z-score standardization), dummy variable traps in nominal categorical encoding, and sparse matrix representations.
* **Application & Problem Solving:** Demonstrated that `ServiceBundleCount` creates strong non-linear retention separation, with churn dropping from 42.2% (0 add-ons) down to 8.6% (5 add-ons).
* **Integration:** Seamlessly connected Bandara's anomaly audit findings to automated data imputation rules, and supplied clean 35-feature matrices directly to Ekanayake's modeling pipeline.
* **Human Dimension & Caring:** Evaluated the ethical implications of synthetic oversampling techniques like SMOTE, electing algorithmic cost weighting (**DEC-06**) to preserve empirical data fidelity and prevent artificial demographic profiles.

---

### 4. Self-Reflection & Future Engineering Outlook
This assignment proved that model accuracy and generalizability are determined far more by preprocessing discipline than by model tuning alone. Establishing automated, leakage-proof transformation pipelines is an indispensable engineering skill that I will carry forward into production AI systems development.
