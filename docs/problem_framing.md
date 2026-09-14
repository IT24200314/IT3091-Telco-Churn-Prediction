# Problem Framing Canvas: Telco Customer Churn Prediction

**Lead Author**: D G N S Widumini (IT24101176) — Problem Framing, Business Strategy & Documentation Lead  
**Group ID**: 2026-AI-07  
**Module**: IT3091 Machine Learning Project  
**Date**: 2026-09-14  

---

## 1. Executive Summary & Problem Context
Customer attrition (churn) directly reduces recurring revenue and increases customer acquisition costs in the telecommunications industry. This project designs, evaluates, and documents a production-grade machine learning classification system to predict individual customer churn risk and empower targeted, proactive retention strategies.

---

## 2. Six Core Problem Framing Dimensions

### 2.1 Primary Stakeholders
- **Chief Marketing Officer (CMO)**: Seeks to preserve monthly recurring revenue (MRR), maximize customer lifetime value (CLV), and allocate retention campaign budgets with measurable return on investment (ROI).
- **Customer Retention & Loyalty Operations Team**: Operational frontline responsible for receiving model-scored churn risk alerts and conducting proactive outbound interventions (discount offers, contract renegotiations, service upgrades, technical support escalations).

### 2.2 Decision Need
- The primary decision need is **proactive churn intervention prior to service cancellation**.
- Rather than reacting to cancellation requests after customers have already decided to leave, the retention team requires timely, probabilistic churn propensity scores to prioritize and tailor high-touch outreach campaigns before contract expiration or month-to-month renewal cycles.

### 2.3 Unit of Analysis
- **Unit of Analysis**: The individual customer subscriber account, uniquely identified by `customerID`.
- Every observation in the feature matrix corresponds to a single account profile capturing demographic traits, subscribed service combinations, contract characteristics, tenure, and billing details.

### 2.4 Target Variable Formulation
- **Target Variable**: `Churn` (Binary Classification)
  - `0` = **Retained / Active Customer** (`No`)
  - `1` = **Churned Customer** (`Yes`)
- **Operational Definition**: Customer terminated their contract/service within the observation window.

### 2.5 Cost Matrix & Asymmetry Analysis
The business cost of prediction errors is fundamentally asymmetric:
- **False Negative (FN) [Cost: HIGH]**: The model predicts that a customer will stay (`0`), but the customer churns (`1`).
  - *Business Impact*: Complete loss of customer lifetime value (average monthly revenue multiplied by expected remaining tenure) plus substantial replacement acquisition costs (CAC is typically 5–7x retention cost).
- **False Positive (FP) [Cost: LOW / MODERATE]**: The model predicts that a customer will churn (`1`), but the customer would have stayed (`0`).
  - *Business Impact*: Minor operational cost of outreach or discount/incentive concession extended to a non-churning customer.
- **Cost Ratio Implication**: $Cost(FN) \gg Cost(FP)$. Therefore, standard default decision thresholds (0.50) are sub-optimal for operational deployment. Threshold tuning must favor higher sensitivity/recall.

### 2.6 Primary Optimization & Evaluation Metrics
- **Recall (Sensitivity)**: Primary metric to minimize costly False Negatives and capture the maximum possible churners.
- **Precision-Recall AUC (PR-AUC)**: Robust benchmark under class imbalance (~26.5% churn prevalence) to prevent over-optimistic assessments.
- **Receiver Operating Characteristic AUC (ROC-AUC)**: Overall discriminative capacity across all candidate decision thresholds.
- **F2-Score**: Harmonic mean weighting recall twice as heavily as precision to balance retention yield against outreach costs.
- *(Note: Raw accuracy is explicitly rejected as a primary decision metric due to the 73.4% / 26.6% class imbalance).*

---

## 3. Scope, Operational Constraints & Ethical Considerations
- **Data Leakage Boundaries**: Strict segregation between train and validation/test pipelines. All imputation, scaling, and categorical encodings must be fitted exclusively on training folds.
- **Operational Feasibility**: Predictions must be accompanied by key driver interpretability (e.g., feature importances / SHAP values) so customer success reps understand the root cause of churn risk during outreach.
- **Algorithmic Fairness**: Ensure retention decisions do not unfairly discriminate or create unintended service disparities across demographic sub-populations (gender, senior citizen status, partner/dependents).
