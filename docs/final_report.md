# IT3091 Machine Learning Project — Master Final Report
## Proactive Churn Risk Prediction and Customer Retention Strategy in Telecommunications

**Group ID:** 2026-AI-07  
**Degree Specialization:** Artificial Intelligence / Data Science, SLIIT Kandy Campus  
**Module:** IT3091 - Machine Learning  

| Member Name | Student ID | Specialization | Core Ownership |
| :--- | :--- | :--- | :--- |
| **U P M U I Ekanayake** *(Leader)* | IT24200314 | AI | Model Selection, Training, 5-Fold Cross-Validation, Diagnostics |
| **D G N S Widumini** | IT24101176 | AI | Business Problem Framing, Master Decision Log, Strategy & Final Report |
| **E J M H D Bandara** | IT24102278 | DS | Exploratory Data Analysis, Data Dictionary, Profiling |
| **H A Wickramathilaka** | IT24100427 | AI | Data Preprocessing Pipeline, Feature Engineering, Leakage Prevention |

---

### 1. Problem Framing & Formulation (5 Marks)
* **Stakeholder:** Telecom Retention Directors and CMO.
* **Decision Need:** Replace reactive cancellations with early-warning risk scoring and tailored retention actions.
* **Primary Decision Lens:** Churn Risk Prediction (Supervised Binary Classification).
* **Secondary Decision Lens:** Retention Segment Analysis (Targeted cohort mapping).
* **Unit of Analysis:** Individual customer account identified by `customerID`.
* **Target Output:** Continuous churn probability $P(\text{Churn}=1 \mid \mathbf{x}) \in [0, 1]$ mapped to High, Medium, and Low risk operational tiers.
* **Optimization Criteria:** Asymmetric cost matrix where $Cost(FN) = \$500$ (lost customer) and $Cost(FP) = \$50$ (retention incentive).

---

### 2. Workflow Diagram & Master Decision Register (10 Marks)
The end-to-end architecture connects business problem framing, visual exploratory analysis, preprocessing, cross-validation, and financial threshold optimization. Detailed interactive diagrams are cataloged in [`docs/workflow_diagram.md`](../docs/workflow_diagram.md) and visual flowchart [`reports/figures/00_workflow_diagram.png`](../reports/figures/00_workflow_diagram.png).

![End-to-End Workflow Architecture](../reports/figures/00_workflow_diagram.png)

Key decisions logged in `docs/decision_log.md`:
* **DEC-01:** Selection of Guided Data Track (Telecom Churn) based on Group ID ending in 7.
* **DEC-02:** Rejection of raw accuracy; optimization focused on ROC-AUC, PR-AUC, and Recall.
* **DEC-03:** Imputation of 11 whitespace instances in `TotalCharges` to `0.0` (all 11 have `tenure = 0`).
* **DEC-04:** Construction of behavioral features (`IsAutomaticPayment`, `ServiceBundleCount`, `TenureCohort`).
* **DEC-05:** Stratified 80/20 train-test split applied strictly before fitting encoders/scalers to prevent data leakage.
* **DEC-06:** Algorithmic class weighting applied instead of synthetic SMOTE to maintain calibrated probabilities.
* **DEC-07:** Stratified 5-Fold Cross-Validation used for all candidate model evaluations.
* **DEC-08:** Logistic Regression with balanced weighting selected as the champion model (CV ROC-AUC: 0.8463, CV Recall: 0.7960).
* **DEC-09:** Asymmetric cost optimization lowering the decision threshold to $\tau^* = 0.44$, reducing business churn loss by $19,250.


---

### 3. Data Understanding & Exploratory Data Analysis (10 Marks)
* **Target Imbalance:** 73.46% (5,174 retained) vs. 26.54% (1,869 churned) — demonstrating why naive accuracy is misleading.
* **The "Tenure Cliff":** Churn heavily peaks in months 1–12 (median tenure of churners is 10 months vs. 38 months for retained customers).
* **Contract Commitment:** Month-to-month contracts exhibit a 42.71% churn rate, compared to 11.27% for 1-year and 2.83% for 2-year commitments.
* **Product Stickiness:** Add-on security and tech support services decrease customer churn rate from 41.7% to 14.6%.

---

### 4. Preprocessing & Feature Engineering Decisions (15 Marks)
* **Leakage Protocol:** Feature transformations isolated strictly to training folds; test fold data remains untouched until final scoring.
* **Type Hygiene:** Whitespace string anomaly in `TotalCharges` resolved and cast to `float64`.
* **Encoding & Scaling:** `OneHotEncoder(drop='first', sparse_output=False)` used for nominal categoricals and `StandardScaler` for continuous numericals.
* **Engineered Features:**
  * `IsAutomaticPayment`: Separates automated payment methods from friction-prone manual check methods.
  * `ServiceBundleCount`: Captures total active add-ons.
  * `TenureCohort`: Bins lifecycle stages into four segments.

---

### 5. Model Strategy & Comparison (20 Marks)
Benchmarking carried out using Stratified 5-Fold Cross-Validation on training data:

| Model Algorithm | 5-Fold CV ROC-AUC | Test ROC-AUC | Test Recall | Test Precision | Test F1-Score | Business Cost @ $\tau^*$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Dummy (Naive Baseline)** | 0.5000 | 0.5000 | 0.0000 | 0.0000 | 0.0000 | $187,000 |
| **Logistic Regression (Champion)** | **0.8463** | **0.8480** | **0.7960** | 0.5178 | **0.6272** | **$34,700** |
| **Random Forest (150 trees)** | 0.8441 | 0.8382 | 0.7217 | 0.5682 | 0.6357 | $52,800 |
| **HistGradientBoosting** | 0.8316 | 0.8439 | 0.4997 | **0.6215** | 0.5538 | $47,650 |
| **SVC (RBF Kernel)** | 0.8294 | 0.8311 | 0.7766 | 0.5157 | 0.6196 | $43,700 |

---

### 6. Evaluation, Validation & Critical Judgement (20 Marks)
* **Model Selection:** Logistic Regression with balanced weighting achieved the highest CV ROC-AUC (0.8463) and captured 79.6% of churners while offering interpretable coefficients.
* **Threshold Tuning:** The probability threshold was optimized from $\tau = 0.50$ to $\tau^* = 0.44$, reducing false negatives and saving \$19,250 in net replacement costs.
* **Attribution:** Log-odds coefficients confirm that `Contract_Two year` ($\beta = -1.38$) and `tenure` ($\beta = -1.24$) act as primary retention anchors, while `InternetService_Fiber optic` ($\beta = +0.73$) and `PaymentMethod_Electronic check` ($\beta = +0.32$) are primary drivers of attrition.

---

### 7. Recommendations, Limitations & Responsible AI (10 Marks)
* **Retention Strategy:** Automated tiered interventions targeting Month-to-Month contracts, automated payment switch incentives, and early 90-day onboarding checkups.
* **Limitations:** Absence of dynamic time-series behavioral records and real-time customer support interactions.
* **Responsible AI:** Fairness audits verified minimal gender performance disparity (recall difference $< 1.5\%$), with explicit safeguards to prevent discriminatory pricing.

---

### 8. Reproducibility & AI-Use Transparency (10 Marks)
* **Reproducibility:** Codebase configured with pinned dependencies in `requirements.txt`, random seed controls (`random_state=42`), and clean runnable Jupyter Notebooks (`01`, `02`, `03`).
* **AI Declaration:** Generative AI tools were utilized transparently to assist with structuring code, refactoring visual layouts, and reviewing documentation, with all logic and results verified by team members.

---

### 9. 3-Minute Video Demonstration & Presentation Deliverable
* **YouTube Video Presentation:** [Click here to view unlisted demo presentation (https://youtu.be/DEMO_LINK)](https://youtu.be/DEMO_LINK)  
  *(Note: Formatted according to the scene-by-scene script in `docs/youtube_demo_script.md`)*
* **Target Duration:** Exactly 180 seconds (3:00 minutes)
* **Team Participation:**
  1. *Scene 1 (0:00–0:35):* Problem Framing & Domain Overview — D G N S Widumini
  2. *Scene 2 (0:35–1:15):* Data Audit, Tenure Cliff & Leak-Free Pipeline — E J M H D Bandara & H A Wickramathilaka
  3. *Scene 3 (1:15–2:15):* 5-Fold Cross-Validation, ROC/PR & Cost Curves — U P M U I Ekanayake
  4. *Scene 4 (2:15–3:00):* 3-Tier Retention Strategy, Financial ROI & Responsible AI — D G N S Widumini

