import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if 'id' in df.columns:
        df.drop('customerID', axis=1, inplace=True)

    cat_cols = df.select_dtypes(include='object').columns
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col].astype(str))

    df.fillna(df.median(numeric_only=True), inplace=True)

    X = df.drop('class', axis=1)
    y = df['class'] 

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    df.to_csv('data/processed/processed_data.csv', index=False)
    return X_scaled, y


def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)
