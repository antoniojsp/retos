import pandas as pd

def preprocess_and_analyze(df, numeric_columns):
    # 1. Create a copy of the original DataFrame
    df_processed = df.copy()

    # 2. Convert Date Column (First column is assumed to be date)
    df_processed.iloc[:, 0] = pd.to_datetime(df_processed.iloc[:, 0], format="%Y-%m-%d")

    # 3. Convert Numeric Columns to numeric
    for col in numeric_columns:
        df_processed[col] = df_processed[col].astype(str).str.replace(r'[$,]', '', regex=True).str.replace('nan', '', regex=False)
        df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce')

    # 4. Fill Missing Values with 0 across entire DataFrame
    df_processed.fillna(0, inplace=True)

    # 5. Calculate Descriptive Statistics by Row
    numeric_df = df_processed[numeric_columns]
    df_processed['row_sum'] = numeric_df.sum(axis=1)
    df_processed['row_mean'] = numeric_df.mean(axis=1)
    df_processed['row_max'] = numeric_df.max(axis=1)
    df_processed['row_min'] = numeric_df.min(axis=1)

    return df_processed

data = {
    "Date": ["2024-07-01", "2024-06-29", "nan"],
    "Revenue": ["$1,500.50", "nan", "$2,300"],
    "Expenses": ["$850.25", "$1,200", "nan"]
}

df = pd.DataFrame(data)
numeric_columns = ["Revenue", "Expenses"]

df_preprocessed = preprocess_and_analyze(df, numeric_columns)

print(df_preprocessed)