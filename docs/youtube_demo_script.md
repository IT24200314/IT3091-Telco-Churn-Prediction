# 3-Minute Video Demo Script & Presentation Flow

**Total Time:** 180 seconds (3:00 minutes)  
**Target Platform:** YouTube (Unlisted Link for Submission)  

---

### Scene 1: Problem Framing & Domain Overview (0:00 – 0:35)
* **Speaker:** D G N S Widumini
* **Visual on Screen:** Slide 1 showing Title, Group ID 2026-AI-07, Stakeholders, and the Problem Framing Canvas.
* **Script:**
  > "Hello everyone. For our IT3091 Machine Learning assignment, Group 2026-AI-07 tackled the Telecommunications domain using the Telco Customer Churn dataset. In telecom, acquiring a new customer costs 5 to 10 times more than retaining an existing one. Our primary lens is Churn Risk Prediction paired with a secondary lens of Retention Segment Analysis. Our goal is to predict customer attrition and provide marketing managers with cost-effective, targeted retention strategies before contracts expire."

---

### Scene 2: EDA & Preprocessing Pipeline (0:35 – 1:15)
* **Speaker:** E J M H D Bandara & H A Wickramathilaka
* **Visual on Screen:** Notebooks `01_eda_and_audit.ipynb` and `02_preprocessing_and_feature_engineering.ipynb` showcasing EDA distribution charts and the feature scaling plot.
* **Script (Bandara):**
  > "During our data audit, we identified a class imbalance of 73.5% staying versus 26.5% leaving. We identified a critical 'Tenure Cliff' in the first 12 months, and discovered that 11 missing values in TotalCharges belonged to new subscribers with zero tenure."
* **Script (Wickramathilaka):**
  > "To strictly prevent data leakage, we stratified the 80/20 train-test split before fitting any transformers. We imputed zero for new accounts, scaled continuous features, and engineered key features like ServiceBundleCount and IsAutomaticPayment to capture customer stickiness."

---

### Scene 3: Modeling, Cross-Validation & Diagnostics (1:15 – 2:15)
* **Speaker:** U P M U I Ekanayake (Leader)
* **Visual on Screen:** Notebook `03_model_training_and_evaluation.ipynb` showing the 5-Fold CV comparison chart, ROC/PR curves, and the Cost Curve plot.
* **Script:**
  > "As team leader, I developed our modeling pipeline. Because raw accuracy is misleading on imbalanced data, we evaluated our baseline and four models using Stratified 5-Fold Cross-Validation, focusing on ROC-AUC, PR-AUC, and Recall. Logistic Regression with balanced weighting emerged as our champion model, achieving a CV ROC-AUC of 0.8463 and capturing 79.6% of churners on the test set. By tuning our probability cutoff to a cost-optimal 0.44 based on an asymmetric business cost matrix, we cut overall retention expenses by over $19,250."

---

### Scene 4: Business Recommendations & Ethics (2:15 – 3:00)
* **Speaker:** D G N S Widumini
* **Visual on Screen:** Feature Importance chart and the 3-Tier Retention Action Matrix.
* **Script:**
  > "Our explainability analysis showed that high-speed Fiber Optic and manual Electronic Check payments are primary churn drivers, while multi-year contracts and bundled security services protect retention. We translated these insights into three operational tiers: high-risk subscribers receive proactive contract restructuring, moderate-risk customers receive free add-on trials and auto-pay discounts, while low-risk customers receive loyalty touchpoints. We verified algorithmic fairness across demographic groups to ensure ethical and unbiased deployment. Thank you!"
