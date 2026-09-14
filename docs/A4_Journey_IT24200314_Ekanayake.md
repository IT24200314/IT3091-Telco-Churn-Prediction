# Individual A4 Personal Learning Journey Report

**Student Name:** U P M U I Ekanayake  
**Student ID:** IT24200314  
**Degree Specialization:** B.Sc. (Hons) in Information Technology — Artificial Intelligence  
**Group ID:** 2026-AI-07  
**Module:** IT3091 Machine Learning Project  
**Assigned Role:** Project Leader, Lead Modeler & ML Systems Evaluator  

---

### 1. Specific Technical Contributions & Ownership
* **Algorithmic Portfolio Implementation:** Engineered and benchmarked five diverse models across three distinct paradigm families: a Naive Prior Dummy Baseline, L2 Regularized Logistic Regression, Random Forest (Bagging), HistGradientBoosting (Boosting), and Support Vector Classifier (RBF Kernel).
* **Stratified Cross-Validation Routine:** Implemented a leakage-proof Stratified 5-Fold Cross-Validation routine strictly within `X_train.csv` to ensure generalizability and eliminate validation variance on our imbalanced target distribution (73.5% vs 26.5%).
* **Diagnostic Evaluation Suite:** Generated comprehensive diagnostic visualizations in `notebooks/03_model_training_and_evaluation.ipynb`, including ROC curves, Precision-Recall (PR) curves, confusion matrix cost heatmaps, and log-odds feature importance rankings.
* **Model Serialization:** Exported the verified champion model to `models/champion_logistic_regression.joblib` and `models/champion_model.joblib`.

---

### 2. Key Technical Hurdle Overcome
* **The Problem:** Under default classification probability cutoffs ($\tau = 0.50$), all candidate models favored the majority class, achieving misleadingly high accuracy while failing to capture critical at-risk churners. In telecommunications, customer replacement acquisition costs ($Cost(FN) = \$500$) are 10x more severe than outreach incentive costs ($Cost(FP) = \$50$).
* **The Solution:** Formulated an asymmetric business loss objective function and mapped the empirical cost curve across continuous probability thresholds $\tau \in [0.05, 0.95]$. Identified the cost-optimal decision threshold at $\tau^* \approx 0.44$, capturing 79.6% of churners and saving **\$19,250 in net churn liability** compared to default thresholding.

---

### 3. Fink's Taxonomy of Significant Learning Alignment
* **Foundational Knowledge:** Mastered loss surface trade-offs between linear margin classifiers, tree-based bagging ensembles, and gradient boosting algorithms on tabular customer churn data.
* **Application & Problem Solving:** Bridged abstract statistical metrics (ROC-AUC 0.8463, PR-AUC 0.6644) directly to financial profit-and-loss balances, proving model utility to executive stakeholders.
* **Integration:** Connected Bandara’s EDA findings (tenure cliff) and Wickramathilaka’s engineered features (`IsAutomaticPayment`, `ServiceBundleCount`) to model explainability log-odds.
* **Human Dimension & Caring:** Ensured algorithmic decision transparency by prioritizing interpretable Logistic Regression over black-box alternatives, ensuring customer care agents understand *why* an account is flagged.

---

### 4. Self-Reflection & Future Engineering Outlook
Leading this project reinforced that the most mathematically complex algorithm is not automatically the best business solution. While HistGradientBoosting provided high precision, Regularized Logistic Regression delivered superior recall, transparent parameter governance, and instant inference. In future ML engineering, I will continue embedding cost-utility frameworks directly into machine learning pipelines.
