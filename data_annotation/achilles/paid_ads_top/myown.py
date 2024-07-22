import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('paid-ads-top-campaigns-table_2023-11-30_2023-12-29.csv')

# Display the first 5 rows
# print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# print(df.to_string())
# Print the column names and  their data types
df = df[(df["Campaign name"] == "Campaign for OUTCOME_SALES") & (df["Created on"] == "2023-08-16")]
print(df["Total sales"].sum())