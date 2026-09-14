import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def load_and_clean_raw(filepath: str) -> pd.DataFrame:
    """Loads raw data and applies structural type casting without data leakage."""
    df = pd.read_csv(filepath)
    
    # Clean whitespace strings in TotalCharges (tenure == 0 indicates new customers)
    df['TotalCharges'] = df['TotalCharges'].replace(' ', '0.0')
    df['TotalCharges'] = df['TotalCharges'].astype(float)
    
    # Standardize target to integer binary
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    
    return df

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Constructs domain-specific features based on customer behavior."""
    df = df.copy()
    
    # 1. Automatic Payment Indicator
    df['IsAutomaticPayment'] = df['PaymentMethod'].apply(
        lambda x: 1 if 'automatic' in str(x).lower() else 0
    )
    
    # 2. Count of Value-Added Services Subscribed
    service_cols = [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
        'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]
    df['ServiceBundleCount'] = df[service_cols].apply(
        lambda row: sum([1 for val in row if val == 'Yes']), axis=1
    )
    
    # 3. Customer Tenure Cohorts
    bins = [-1, 12, 24, 48, 72]
    labels = ['Cohort_0_12m', 'Cohort_13_24m', 'Cohort_25_48m', 'Cohort_49_72m']
    df['TenureCohort'] = pd.cut(df['tenure'], bins=bins, labels=labels)
    
    return df

def build_preprocessing_pipeline():
    """Builds a scikit-learn ColumnTransformer for modular transformation."""
    num_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'ServiceBundleCount']
    cat_features = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
        'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
        'Contract', 'PaperlessBilling', 'PaymentMethod', 'IsAutomaticPayment', 'TenureCohort'
    ]
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_features),
            ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), cat_features)
        ]
    )
    return preprocessor, num_features, cat_features

def run_pipeline(input_path: str, output_dir: str):
    """Executes stratified train-test split before fit-transform to strictly prevent leakage."""
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Load and engineer features
    raw_df = load_and_clean_raw(input_path)
    featured_df = engineer_features(raw_df)
    
    # Drop primary key identifier
    X = featured_df.drop(columns=['customerID', 'Churn'])
    y = featured_df['Churn']
    
    # 2. Stratified Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    
    print(f"Train Set Shape: {X_train.shape}, Test Set Shape: {X_test.shape}")
    print(f"Train Churn Rate: {y_train.mean():.4f}, Test Churn Rate: {y_test.mean():.4f}")
    
    # 3. Fit transformer ONLY on training data
    preprocessor, num_cols, cat_cols = build_preprocessing_pipeline()
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)
    
    # 4. Extract generated feature names
    cat_encoder = preprocessor.named_transformers_['cat']
    encoded_cat_names = cat_encoder.get_feature_names_out(cat_cols)
    all_feature_names = list(num_cols) + list(encoded_cat_names)
    
    # 5. Convert to DataFrames and save
    X_train_df = pd.DataFrame(X_train_transformed, columns=all_feature_names)
    X_test_df = pd.DataFrame(X_test_transformed, columns=all_feature_names)
    
    X_train_df.to_csv(os.path.join(output_dir, 'X_train.csv'), index=False)
    X_test_df.to_csv(os.path.join(output_dir, 'X_test.csv'), index=False)
    y_train.to_csv(os.path.join(output_dir, 'y_train.csv'), index=False)
    y_test.to_csv(os.path.join(output_dir, 'y_test.csv'), index=False)
    
    print(f"Transformed features saved successfully to {output_dir}")
    print(f"Total processed feature count: {len(all_feature_names)}")

if __name__ == '__main__':
    run_pipeline(
        input_path='data/WA_Fn-UseC_-Telco-Customer-Churn.csv',
        output_dir='data/processed'
    )
