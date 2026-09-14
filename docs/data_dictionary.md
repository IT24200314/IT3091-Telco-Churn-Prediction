# Telco Customer Churn — Data Dictionary

**Unit of Analysis / Row Meaning:** Each row represents an individual telecommunications subscriber account identified by a unique `customerID`, detailing their demographic attributes, subscribed service features, billing arrangements, and churn status.

| Variable Name | Semantic Description | Data Type | Value Range / Categories | Business Role |
| :--- | :--- | :--- | :--- | :--- |
| `customerID` | Unique subscriber account identifier | Categorical (Nominal) | Alphanumeric (e.g., `7590-VHVEG`) | Primary Key (Excluded from modeling) |
| `gender` | Subscriber's recorded biological gender | Categorical (Binary) | `Male`, `Female` | Demographic feature |
| `SeniorCitizen` | Indicator if subscriber is 65 years or older | Categorical (Binary) | `0` (No), `1` (Yes) | Demographic feature |
| `Partner` | Indicator if subscriber has a domestic partner | Categorical (Binary) | `Yes`, `No` | Demographic feature |
| `Dependents` | Indicator if subscriber lives with dependents | Categorical (Binary) | `Yes`, `No` | Demographic feature |
| `tenure` | Total months subscriber has stayed with the company | Numerical (Discrete) | `0` to `72` months | Customer loyalty proxy |
| `PhoneService` | Indicator if subscriber has telephone service | Categorical (Binary) | `Yes`, `No` | Base service feature |
| `MultipleLines` | Subscription status for multiple telephone lines | Categorical (Nominal) | `Yes`, `No`, `No phone service` | Add-on service |
| `InternetService`| Subscriber's internet connection technology | Categorical (Nominal) | `DSL`, `Fiber optic`, `No` | Core service tier |
| `OnlineSecurity` | Add-on cyber security protection subscription | Categorical (Nominal) | `Yes`, `No`, `No internet service` | Value-added service |
| `OnlineBackup` | Add-on cloud backup subscription | Categorical (Nominal) | `Yes`, `No`, `No internet service` | Value-added service |
| `DeviceProtection`| Add-on equipment hardware warranty | Categorical (Nominal) | `Yes`, `No`, `No internet service` | Value-added service |
| `TechSupport` | Dedicated technical customer support tier | Categorical (Nominal) | `Yes`, `No`, `No internet service` | Value-added service |
| `StreamingTV` | Subscription to stream digital television | Categorical (Nominal) | `Yes`, `No`, `No internet service` | Content service |
| `StreamingMovies`| Subscription to stream digital movie catalog | Categorical (Nominal) | `Yes`, `No`, `No internet service` | Content service |
| `Contract` | Billing contract terms commitment | Categorical (Nominal) | `Month-to-month`, `One year`, `Two year` | Structural commitment |
| `PaperlessBilling`| Opt-in status for electronic digital billing | Categorical (Binary) | `Yes`, `No` | Operational preference |
| `PaymentMethod` | Preferred transaction channel for billing | Categorical (Nominal) | `Electronic check`, `Mailed check`, `Bank transfer (automatic)`, `Credit card (automatic)` | Billing behavior |
| `MonthlyCharges` | Amount billed monthly to subscriber | Numerical (Continuous)| `$18.25` to `$118.75` | Financial revenue feature |
| `TotalCharges` | Cumulative historical charges billed to date | Numerical (Continuous)| `$18.80` to `$8684.80` (Contains 11 blank strings) | Financial revenue feature |
| `Churn` | Subscriber status in the last evaluated cycle | Categorical (Binary) | `Yes` (1), `No` (0) | Target Variable |
