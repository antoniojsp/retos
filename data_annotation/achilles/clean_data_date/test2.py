import pandas as pd


def preprocess_and_analyze(df, currency_cols):
    """
    Preprocesses a DataFrame containing currency data, standardizes dates,
    calculates row-wise statistics, and appends them to both the original
    and processed DataFrames.

    Args:
        df: The DataFrame to preprocess.
        currency_cols: A list of column names containing currency values.

    Returns:
        A modified copy of the original DataFrame with added statistics columns.
    """

    # Create a copy to avoid modifying the original DataFrame
    df_processed = df.copy()

    # Convert the first column (assumed to be date) to datetime
    df_processed[df_processed.columns[0]] = pd.to_datetime(
        df_processed[df_processed.columns[0]], format="%Y-%m-%d"
    )

    # Clean and convert currency columns to numeric
    for col in currency_cols:
        df_processed[col] = (
            df_processed[col]
            .astype(str)
            .str.replace(r"[$,]", "", regex=True)
            .str.replace(",", ".", regex=False)  # Adjust for potential European format
        )
        df_processed[col] = pd.to_numeric(df_processed[col], errors="coerce")

    # Fill null values with zeros in the processed DataFrame
    df_processed = df_processed.fillna(0)

    # Calculate row-wise statistics (excluding the date column)
    numeric_cols = [col for col in currency_cols if pd.api.types.is_numeric_dtype(df_processed[col])]
    df_processed["row_sum"] = df_processed[numeric_cols].sum(axis=1)
    df_processed["row_mean"] = df_processed[numeric_cols].mean(axis=1)
    df_processed["row_min"] = df_processed[numeric_cols].min(axis=1)
    df_processed["row_max"] = df_processed[numeric_cols].max(axis=1)

    # Append the statistics columns to the original DataFrame as well
    df["row_sum"] = df_processed["row_sum"]
    df["row_mean"] = df_processed["row_mean"]
    df["row_min"] = df_processed["row_min"]
    df["row_max"] = df_processed["row_max"]

    return df_processed  # Or return df if you prefer the original with added columns


# Sample DataFrame with currency and date inconsistencies
data = {
    "Date": ["2024-07-01", "2024-06-28", "2024-06-25"],
    "Sales": ["$1,250.50", "$875", "1200"],
    "Expenses": ["$500", None, "$350.25"],
    "Profit": ["$750.50", "875", None],
}
df = pd.DataFrame(data)

currency_columns = ["Sales", "Expenses", "Profit"]  # List of currency columns

result_df = preprocess_and_analyze(df, currency_columns)
print(df.to_string())
print(result_df.to_string())

