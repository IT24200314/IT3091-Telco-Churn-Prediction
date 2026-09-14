# Central Decision Log: Telco Customer Churn Prediction

**Maintained by**: D G N S Widumini (IT24101176) — Problem Framing, Business Strategy & Documentation Lead  
**Group ID**: 2026-AI-07  
**Module**: IT3091 Machine Learning Project  

---

## Decision Tracking Register

| Decision ID | Date | Stage | Options Considered | Decision Chosen | Justification / Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DEC-01** | 2026-09-14 | Setup | Kaggle Guided Track vs. Industry Explorer | **Guided Data Track (Telco)** | Aligned with Group ID `2026-AI-07` final digit 7 requirement. Tabular classification with rich service combinations. |
| **DEC-02** | 2026-09-14 | Problem Framing | Churn Risk vs. Customer Lifetime Value (CLV) | **Churn Risk Classification + Segment Analysis** | Operational priority for retention outreach. Primary metrics: Recall, PR-AUC, ROC-AUC over deceptive raw accuracy. |
| **DEC-03** | 2026-09-14 | Data Cleaning | Drop 11 blank rows vs. Impute with 0 | **Impute `TotalCharges` = 0.0** | 100% of blank records have `tenure = 0` (new subscribers before first invoice). Eliminates data loss and avoids survivor bias. |
| **DEC-04** | 2026-09-14 | Feature Engineering | Raw features only vs. Domain-specific behavioral features | **Engineer `IsAutomaticPayment`, `ServiceBundleCount`, `TenureCohort`** | Visual EDA confirms strong non-linear separation: automatic payment reduces churn 2.4x; bundle adoption reduces churn from 42.2% to 8.6%; tenure cohorts capture 0-12m tenure cliff. |
| **DEC-05** | 2026-09-14 | Leakage Prevention | Full-dataset scaling vs. Fit on Train only | **Fit `ColumnTransformer` strictly on `X_train`** | Stratified 80/20 train/test split executed prior to fitting scalers/encoders. Prevents optimistic test leakage ($\mu, \sigma$). |
| **DEC-06** | 2026-09-14 | Class Imbalance | Synthetic oversampling (SMOTE) vs. Cost-sensitive weighting | **Algorithmic Cost Weighting (`balanced`)** | Preserves empirical feature distributions in test data; avoids synthetic artifacts in high-dimensional one-hot encoded spaces. |

---

## Log Maintenance Protocol
1. Any architectural, pre-processing, feature engineering, modeling, or deployment change must receive a registered decision entry.
2. Every entry must detail alternatives considered, operational tradeoffs, and empirical evidence guiding the selection.
3. Review and sign-off are coordinated by the Documentation Lead in consultation with relevant technical owners.
