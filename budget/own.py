import pandas as pd

# Read the csv file
df = pd.read_csv("ExportedTransactions.csv")

# Display the first 5 rows
print(df.head())

# Display column names and their types
print(df.to_string())
print(df["Amount"].sum())