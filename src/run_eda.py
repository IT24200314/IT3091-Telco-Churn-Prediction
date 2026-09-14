import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set overall plotting aesthetics
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.sans-serif': 'Arial', 'font.size': 11})

# Ensure destination directory exists
os.makedirs('reports/figures', exist_ok=True)

# 1. Load Dataset
data_path = 'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(data_path)

print(f"Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# 2. Audit TotalCharges blanks and clean for EDA purposes
blank_mask = df['TotalCharges'] == ' '
print(f"Total charges whitespace count: {blank_mask.sum()}")
df.loc[blank_mask, 'TotalCharges'] = '0.0'
df['TotalCharges'] = df['TotalCharges'].astype(float)
df['Churn_Numeric'] = df['Churn'].map({'Yes': 1, 'No': 0})

# --- Figure 1: Target Variable Imbalance ---
plt.figure(figsize=(6, 5))
churn_counts = df['Churn'].value_counts(normalize=True) * 100
ax = sns.barplot(x=churn_counts.index, y=churn_counts.values, palette=['#2b5c8f', '#d95f02'])
plt.title('Target Variable Distribution (Churn Ratio)', fontsize=13, weight='bold')
plt.ylabel('Percentage of Subscribers (%)')
plt.xlabel('Customer Churned?')
for p in ax.patches:
    ax.annotate(f"{p.get_height():.2f}%", (p.get_x() + p.get_width() / 2., p.get_height() / 2),
                ha='center', va='center', color='white', weight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('reports/figures/01_churn_distribution.png', dpi=300)
plt.close()

# --- Figure 2: Numerical Feature Distributions by Churn ---
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
num_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
titles = ['Customer Tenure (Months)', 'Monthly Charges ($)', 'Total Cumulative Charges ($)']

for i, col in enumerate(num_features):
    sns.kdeplot(data=df, x=col, hue='Churn', common_norm=False, fill=True, 
                palette=['#2b5c8f', '#d95f02'], alpha=0.4, ax=axes[i])
    axes[i].set_title(titles[i], fontsize=12, weight='bold')
    axes[i].set_ylabel('Density')
plt.tight_layout()
plt.savefig('reports/figures/02_numerical_distributions.png', dpi=300)
plt.close()

# --- Figure 3: Contract Type & Internet Service Churn Rates ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Contract Churn Rate
contract_churn = df.groupby('Contract')['Churn_Numeric'].mean().reset_index()
contract_churn['Churn_Rate_%'] = contract_churn['Churn_Numeric'] * 100
sns.barplot(data=contract_churn, x='Contract', y='Churn_Rate_%', ax=axes[0], palette='Blues_r')
axes[0].set_title('Churn Rate by Contract Commitment', fontsize=12, weight='bold')
axes[0].set_ylabel('Churn Rate (%)')
for p in axes[0].patches:
    axes[0].annotate(f"{p.get_height():.1f}%", (p.get_x() + p.get_width() / 2., p.get_height() + 1),
                     ha='center', fontsize=11)

# Internet Service Churn Rate
internet_churn = df.groupby('InternetService')['Churn_Numeric'].mean().reset_index()
internet_churn['Churn_Rate_%'] = internet_churn['Churn_Numeric'] * 100
sns.barplot(data=internet_churn, x='InternetService', y='Churn_Rate_%', ax=axes[1], palette='Oranges_r')
axes[1].set_title('Churn Rate by Internet Service Tier', fontsize=12, weight='bold')
axes[1].set_ylabel('Churn Rate (%)')
for p in axes[1].patches:
    axes[1].annotate(f"{p.get_height():.1f}%", (p.get_x() + p.get_width() / 2., p.get_height() + 1),
                     ha='center', fontsize=11)

plt.tight_layout()
plt.savefig('reports/figures/03_churn_by_contract_and_internet.png', dpi=300)
plt.close()

# --- Figure 4: Payment Method Churn Rate ---
plt.figure(figsize=(10, 5))
pm_churn = df.groupby('PaymentMethod')['Churn_Numeric'].mean().reset_index().sort_values('Churn_Numeric', ascending=False)
pm_churn['Churn_Rate_%'] = pm_churn['Churn_Numeric'] * 100
ax = sns.barplot(data=pm_churn, x='Churn_Rate_%', y='PaymentMethod', palette='viridis')
plt.title('Churn Rate Across Payment Methods', fontsize=13, weight='bold')
plt.xlabel('Churn Rate (%)')
for p in ax.patches:
    ax.annotate(f"{p.get_width():.1f}%", (p.get_width() + 1, p.get_y() + p.get_height() / 2.),
                va='center', fontsize=10)
plt.xlim(0, 55)
plt.tight_layout()
plt.savefig('reports/figures/04_churn_by_payment_method.png', dpi=300)
plt.close()

# --- Figure 5: Numerical Correlation Matrix ---
plt.figure(figsize=(6, 5))
corr = df[['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn_Numeric']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, square=True)
plt.title('Correlation Matrix (Numerical Features & Churn)', fontsize=12, weight='bold')
plt.tight_layout()
plt.savefig('reports/figures/05_numerical_correlation_matrix.png', dpi=300)
plt.close()

print("All figures successfully exported to reports/figures/")
