import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('synop_evento_SAEZ.csv')
print(df.head())
# Display the first 5 rows
# print(df.head().to_markdown(index=False, numalign="left", stralign="left"))
# print(df.to_string())
grouped = df.groupby(['año', 'mes'])['t'].mean().reset_index()
# Print the column names and their data types
# print(grouped.to_string())

# range_values = df[.max() - df.min()
# print("Range values:")
# print(range_values)