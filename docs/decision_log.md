# Central Decision Log: Telco Customer Churn Prediction

**Maintained by**: D G N S Widumini (IT24101176) — Problem Framing, Business Strategy & Documentation Lead  
**Group ID**: 2026-AI-07  
**Module**: IT3091 Machine Learning Project  

---

## Decision Tracking Register

| Decision ID | Date | Stage | Options Considered | Decision Chosen | Justification / Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DEC-01** | 2026-09-14 | Setup | Kaggle Guided Track vs. Industry Explorer | **Guided Data Track (Telco)** | Aligned with Group ID `2026-AI-07` final digit 7 requirement. Dataset structure matches all mandatory requirements for tabular classification and retention analysis. |
| **DEC-02** | 2026-09-14 | Problem Framing | Churn Risk vs. Customer Lifetime Value (CLV) Regression | **Churn Risk Classification + Segment Analysis** | Immediate operational relevance for subscriber retention workflows. Retention reps require actionable churn probability scores and categorical churn flags. |
| **DEC-03** | 2026-09-14 | Preprocessing Audit | Drop 11 blank rows vs. Impute with 0 | **Impute `TotalCharges` = 0.0** | All 11 records possess `tenure = 0`, signifying brand new customer accounts that have not completed their first billing cycle. Dropping them introduces unnecessary data loss and survivor bias. |

---

## Log Maintenance Protocol
1. Any architectural, pre-processing, feature engineering, modeling, or deployment change must receive a registered decision entry.
2. Every entry must detail alternatives considered, operational tradeoffs, and empirical evidence guiding the selection.
3. Review and sign-off are coordinated by the Documentation Lead in consultation with relevant technical owners.
