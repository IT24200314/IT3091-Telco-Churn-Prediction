# Individual A4 Personal Learning Journey Report

**Student Name:** E J M H D Bandara  
**Student ID:** IT24102278  
**Degree Specialization:** B.Sc. (Hons) in Information Technology — Data Science  
**Group ID:** 2026-AI-07  
**Module:** IT3091 Machine Learning Project  
**Assigned Role:** Data Understanding & Exploratory Data Analysis (EDA) Lead  

---

### 1. Specific Technical Contributions & Ownership
* **Formal Data Dictionary Construction:** Designed `docs/data_dictionary.md`, cataloging all 21 raw features with semantic definitions, data types, legitimate value ranges, and assigned business roles.
* **Interactive Visual EDA Pipeline:** Authored and executed `notebooks/01_eda_and_audit.ipynb` spanning 8 analytical sections, embedding publication-quality charts for distributions, correlations, and segment attrition rates.
* **Statistical Anomaly Auditing:** Discovered and audited 11 anomalous whitespace records (`" "`) in `TotalCharges`, analyzing their structural characteristics against subscriber tenure.
* **Standalone Execution Script:** Implemented `src/run_eda.py`, exporting verified high-resolution visualization figures to `reports/figures/`.

---

### 2. Key Technical Hurdle Overcome
* **The Problem:** The `TotalCharges` attribute was improperly inferred as an `object` data type due to 11 blank space characters. Standard automated cleaning routines would either drop these 11 rows (causing data loss and survivor bias) or impute them with mean/median values (distorting financial metrics).
* **The Solution:** Conducted targeted cross-variable grouping and proved that 100% of the blank records possessed `tenure = 0`. These represented newly onboarded subscribers who had not yet received their first monthly invoice. Formulated **DEC-03** to impute `TotalCharges = 0.0` and cast the column to `float64`, preserving dataset integrity without distorting historical billing distributions.

---

### 3. Fink's Taxonomy of Significant Learning Alignment
* **Foundational Knowledge:** Solidified deep theoretical understanding of univariate, bivariate, and multivariate statistical profiling, KDE density estimation, and point-biserial correlation metrics.
* **Application & Problem Solving:** Identified the "Tenure Cliff" phenomenon (months 1–6 showing peak attrition hazard) and mathematically demonstrated how naive classification accuracy fails under a 73.5% / 26.5% imbalanced distribution.
* **Integration:** Handed off clear empirical evidence to Wickramathilaka (preprocessing) and Ekanayake (modeling), recommending specific feature transformations (`TenureCohort`, `ServiceBundleCount`) based on observed non-linearities.
* **Human Dimension & Caring:** Analyzed billing friction across customer segments, highlighting how manual payment channels create unnecessary operational anxiety for consumers.

---

### 4. Self-Reflection & Future Engineering Outlook
As a Data Science student, this module reinforced that modeling success is entirely contingent on data understanding rigor. Skipping deep exploratory profiling would have left anomalies undetected and led our team into naive metric traps. In future data science projects, I will champion visual-first, hypothesis-driven exploratory workflows.
