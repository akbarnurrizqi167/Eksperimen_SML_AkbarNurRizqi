import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path='dataset_raw/WA_Fn-UseC_-Telco-Customer-Churn.csv'):
    print("[INFO] Loading dataset...")
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    print("[INFO] Preprocessing dataset...")

    # Drop customerID
    df.drop(columns=['customerID'], inplace=True)

    # Konversi TotalCharges ke float
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

    # Encode target
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})

    # One-hot encoding untuk fitur kategorikal
    categorical_cols = df.select_dtypes(include='object').columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Normalisasi fitur numerik
    num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df

def split_and_save(df, output_dir='preprocessing/dataset_preprocessing'):
    print("[INFO] Splitting dataset...")

    X = df.drop(columns=['Churn'])
    y = df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # Gabungkan kembali untuk simpan
    train_df = X_train.copy()
    train_df['target'] = y_train

    test_df = X_test.copy()
    test_df['target'] = y_test

    os.makedirs(output_dir, exist_ok=True)

    train_df.to_csv(os.path.join(output_dir, 'train.csv'), index=False)
    test_df.to_csv(os.path.join(output_dir, 'test.csv'), index=False)

    print(f"[SUCCESS] Data saved to '{output_dir}'")

def main():
    df = load_data()
    df_clean = preprocess_data(df)
    split_and_save(df_clean)

if __name__ == "__main__":
    main()