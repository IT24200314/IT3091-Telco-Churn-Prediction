# Individual A4 Personal Learning Journey Report Templates

Each member must export a **1-page A4 PDF report** detailing their individual contributions and learning journey for individual grading.

---

### Template 1: U P M U I Ekanayake (IT24200314) — AI Specialization
* **Role:** Team Leader, Lead Modeler & Systems Evaluator
* **Key Sections for A4 Page:**
  1. *Specific Technical Contribution:* Implemented baseline and four candidate models (Dummy, Logistic Regression, Random Forest, HistGradientBoosting, SVC). Designed Stratified 5-Fold Cross-Validation pipeline and holdout test evaluation.
  2. *Key Technical Hurdle Overcome:* Recognizing that standard 0.5 probability cutoffs are sub-optimal for imbalanced real-world costs. Solved this by building an empirical cost-loss curve across thresholds, identifying $\tau^* = 0.44$ to save \$19,250.
  3. *Fink Alignment (Integration & Problem Solving):* Integrated business financial losses into model evaluation metrics, connecting technical AI decisions to organizational ROI.
  4. *What I Learned:* Practical machine learning requires balancing model complexity with interpretability. While gradient boosting had strong precision, regularized logistic regression delivered superior recall, faster training, and transparent log-odds for business stakeholders.

---

### Template 2: D G N S Widumini (IT24101176) — AI Specialization
* **Role:** Business Problem Framing, Master Decision Log & Strategy Lead
* **Key Sections for A4 Page:**
  1. *Specific Technical Contribution:* Developed Problem Framing Canvas, maintained the 9-entry Master Decision Log, authored the final report, and created the 3-tier retention strategy matrix.
  2. *Key Technical Hurdle Overcome:* Translating raw machine learning coefficients into operational marketing initiatives without resorting to margin-diluting blanket discounts.
  3. *Fink Alignment (Human Dimension & Responsible AI):* Evaluated fairness and parity across demographic attributes, ensuring ethical and non-discriminatory retention practices.
  4. *What I Learned:* An AI model has no value unless business workflows can operationalize its outputs. Clear documentation and decision logs are vital for cross-team collaboration.

---

### Template 3: E J M H D Bandara (IT24102278) — DS Specialization
* **Role:** Data Understanding & Exploratory Data Analysis Lead
* **Key Sections for A4 Page:**
  1. *Specific Technical Contribution:* Built the formal 21-variable Data Dictionary and implemented the 8-section visual exploratory analysis notebook (`01_eda_and_audit.ipynb`).
  2. *Key Technical Hurdle Overcome:* Investigating the 11 blank strings in `TotalCharges` and statistically proving that all 11 instances corresponded to `tenure = 0` new subscribers, preventing incorrect data deletion.
  3. *Fink Alignment (Foundational Knowledge & Data Literacy):* Demonstrated statistical reasoning across distributions, identifying the 0–12 month "tenure cliff" and service stickiness correlations.
  4. *What I Learned:* Thorough exploratory data analysis establishes the foundation for the entire modeling lifecycle. Inspecting raw distributions prevented naive metric traps early in the project.

---

### Template 4: H A Wickramathilaka (IT24100427) — AI Specialization
* **Role:** Data Preprocessing & Feature Engineering Pipeline Lead
* **Key Sections for A4 Page:**
  1. *Specific Technical Contribution:* Built the leakage-proof preprocessing pipeline using `ColumnTransformer`, standard scaling, and one-hot encoding. Engineered `ServiceBundleCount`, `IsAutomaticPayment`, and `TenureCohort`.
  2. *Key Technical Hurdle Overcome:* Ensuring strict data leakage prevention by executing stratified train-test splits before fitting transformations.
  3. *Fink Alignment (Application & ML Implementation):* Evaluated class imbalance handling options, choosing algorithmic cost weighting over synthetic SMOTE to preserve probability calibration.
  4. *What I Learned:* Preprocessing decisions fundamentally determine model ceiling performance. Clean, reproducible scikit-learn pipelines prevent subtle data contamination errors.
