# IT3091: Telco Customer Churn Prediction & Retention Optimization

![Python Version](https://img.shields.io/badge/Python-3.11%20%7C%203.14-blue)
![Machine Learning](https://img.shields.io/badge/Domain-Machine%20Learning%20%26%20Predictive%20Analytics-green)
![Course](https://img.shields.io/badge/SLIIT-IT3091%20Machine%20Learning-orange)
![Build Status](https://img.shields.io/badge/Pipeline-Verified%20%26%20Leak--Free-success)

## 📌 Project Overview
This repository hosts the production-ready machine learning system for predicting customer churn in a telecommunications subscription service. By uniting statistical profiling, modular preprocessing, multi-model cross-validation, asymmetric cost optimization, and transparent AI governance, this project provides marketing and retention stakeholders with calibrated churn propensity scores and high-ROI operational retention strategies.

---

## 👥 Project Team & Core Responsibilities

| Member Name | Student ID | Email | Degree Specialization | Core Assignment Responsibility |
| :--- | :--- | :--- | :--- | :--- |
| **U P M U I Ekanayake** *(Leader)* | IT24200314 | `it24200314@my.sliit.lk` | AI | **Lead Modeler & ML Systems Evaluator** |
| **D G N S Widumini** | IT24101176 | `it24101176@my.sliit.lk` | AI | **Problem Framing, Business Strategy & Documentation Lead** |
| **E J M H D Bandara** | IT24102278 | `it24102278@my.sliit.lk` | DS | **Data Understanding & Exploratory Data Analysis (EDA)** |
| **H A Wickramathilaka** | IT24100427 | `it24100427@my.sliit.lk` | AI | **Preprocessing & Feature Engineering Pipeline Lead** |

---

## 📁 Repository Structure
```plaintext
IT3091-Telco-Churn-Prediction/
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Raw Dataset (SHA256: 16320c9c..., 7,043 rows)
├── docs/
│   ├── problem_framing.md                        # Six problem framing dimensions & cost matrix
│   ├── workflow_diagram.md                       # Mermaid & visual flowchart architecture
│   ├── data_dictionary.md                        # 21-variable schema, semantics & SHA-256 hash
│   ├── decision_log.md                           # Master Decision Log (DEC-01 to DEC-09)
│   ├── eda_insight_log.md                        # Empirical EDA findings & tenure cliff analysis
│   ├── preprocessing_log.md                      # Leakage prevention & transformation rationale
│   ├── business_recommendations.md               # 3-Tier retention playbook & ROI analysis
│   ├── final_report.md                           # Master final synthesis report (All 8 rubric criteria)
│   ├── ai_transparency_declaration.md            # AI-use disclosure & academic integrity declaration
│   ├── youtube_demo_script.md                    # 3-minute video presentation script
│   ├── personal_learning_journey_templates.md    # Summary templates for individual grading
│   ├── A4_Journey_IT24200314_Ekanayake.md        # Individual A4 Report: Lead Modeler & Evaluator
│   ├── A4_Journey_IT24101176_Widumini.md         # Individual A4 Report: Strategy & Docs Lead
│   ├── A4_Journey_IT24102278_Bandara.md          # Individual A4 Report: Data Understanding & EDA
│   └── A4_Journey_IT24100427_Wickramathilaka.md  # Individual A4 Report: Preprocessing Pipelines
├── models/
│   ├── champion_logistic_regression.joblib       # Serialized champion model weights
│   ├── champion_model.joblib                     # Champion model backup
│   └── preprocessor.joblib                       # Serialized fitted ColumnTransformer pipeline
├── notebooks/
│   ├── 01_eda_and_audit.ipynb                    # 8-section visual exploratory analysis
│   ├── 02_preprocessing_and_feature_engineering.ipynb # Leak-free pipeline & before/after scaling
│   └── 03_model_training_and_evaluation.ipynb    # 5-Fold CV, ROC/PR curves & cost thresholding
├── reports/
│   ├── cv_model_comparison.csv                   # Cross-validation quantitative benchmark metrics
│   └── figures/                                  # 10 publication-grade visualization artifacts
│       ├── 00_workflow_diagram.png               # End-to-end decision architecture flowchart
│       └── 01 to 09 diagnostic plots             # Distributions, correlations, ROC, PR, cost curves
├── src/
│   ├── run_eda.py                                # Visual EDA script
│   ├── preprocessing.py                          # Modular ColumnTransformer pipeline
│   └── train_and_evaluate.py                     # Multi-model cross-validation & evaluation script
├── .gitignore                                    # Git ignore rules for venv, checkpoints, cache
├── requirements.txt                              # Pinned dependencies for 100% reproducibility
├── LICENSE                                       # Project license
└── README.md                                     # Master documentation hub

```

---

## 📊 Model Benchmark Summary (Stratified 5-Fold Cross-Validation)

| Classifier Model | CV ROC-AUC | CV PR-AUC | Test ROC-AUC | Test Recall | Test F1 | Total Business Cost @ $\tau^*$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Dummy (Naive Baseline)** | 0.5000 | 0.2654 | 0.5000 | 0.0000 | 0.0000 | $187,000 |
| **Logistic Regression (L2)** 🏆 | **0.8463** | **0.6644** | **0.8480** | **0.7960** | **0.6272** | **$34,700** ($\tau^* \approx 0.44$) |
| **Random Forest (Bagging)** | 0.8441 | 0.6559 | 0.8382 | 0.7217 | 0.6357 | $52,800 ($\tau^* \approx 0.38$) |
| **HistGradientBoosting** | 0.8316 | 0.6354 | 0.8439 | 0.4997 | 0.5538 | $47,650 ($\tau^* \approx 0.28$) |
| **SVC (RBF Kernel)** | 0.8294 | 0.6103 | 0.8311 | 0.7766 | 0.6196 | $43,700 ($\tau^* \approx 0.42$) |

---

## ⚙️ Quickstart & Reproduction Guide

```bash
# 1. Clone the repository
git clone https://github.com/IT24200314/IT3091-Telco-Churn-Prediction.git
cd IT3091-Telco-Churn-Prediction

# 2. Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# 3. Install pinned dependencies
pip install -r requirements.txt

# 4. Run any visual notebook
jupyter notebook notebooks/01_eda_and_audit.ipynb
jupyter notebook notebooks/02_preprocessing_and_feature_engineering.ipynb
jupyter notebook notebooks/03_model_training_and_evaluation.ipynb
```
