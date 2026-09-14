# IT3091: Telco Customer Churn Prediction & Retention Optimization

![Python Version](https://img.shields.io/badge/Python-3.11%20%7C%203.14-blue)
![Machine Learning](https://img.shields.io/badge/Domain-Machine%20Learning%20%26%20Predictive%20Analytics-green)
![Course](https://img.shields.io/badge/SLIIT-IT3091%20Machine%20Learning-orange)

## 📌 Project Overview
This repository contains the end-to-end Machine Learning project for predicting customer churn in a telecommunications subscription service. By leveraging statistical profiling, machine learning classification algorithms, cost-sensitive threshold optimization, and transparent AI documentation, this project equips stakeholders with actionable churn propensity scores and targeted customer retention strategies.

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
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Telco Churn Raw Dataset (7,043 rows, 21 columns)
├── docs/
│   ├── problem_framing.md                    # Six problem framing dimensions & cost matrix
│   └── decision_log.md                       # Master architectural and preprocessing decision log
├── notebooks/
│   └── 01_eda_and_audit.ipynb                # Initial data audit, dimensions & anomaly inspection
├── src/                                      # Modular source code pipelines
├── .gitignore                                # Git ignore rules for venv, checkpoints, and cache
├── requirements.txt                          # Pinned project dependencies for reproducibility
├── LICENSE                                   # Repository license
└── README.md                                 # Project documentation
```

---

## ⚙️ Environment Setup & Reproduction Guide

### 1. Clone the Repository
```bash
git clone https://github.com/IT24200314/IT3091-Telco-Churn-Prediction.git
cd IT3091-Telco-Churn-Prediction
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (CMD):
.\venv\Scripts\activate.bat
# Linux / macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Baseline Inspection Notebook
```bash
jupyter notebook notebooks/01_eda_and_audit.ipynb
```

---

## 🔍 Key Findings from Initial Audit
- **Dataset Dimensions**: 7,043 customer records across 21 feature columns.
- **Target Distribution**: Retained (`No`) = 73.46%, Churned (`Yes`) = 26.54% (~3:1 class imbalance).
- **Data Quality Anomaly**: 11 records possess blank whitespace (`" "`) in `TotalCharges`. All 11 records have `tenure = 0` (brand-new accounts prior to their first billing cycle). As documented in **DEC-03**, these are imputed with `0.0` to eliminate data loss and prevent survivor bias.
