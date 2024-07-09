import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv("WELLNESS_COST_2022_CW_V2 - Sheet1.tsv", sep='\t')

# Display the first 5 rows
print(df.head())

# Print the column names and their data types
print(df.info())
grouped = (
    df.groupby(['JOB DESC', 'CONCEPT'])[['TOTAL']]
    .sum()
    .unstack('CONCEPT')
    .fillna(0)
)
print(grouped.transpose().to_markdown())

# Print the first 5 rows
print(grouped.head())

# Filter rows where the total is greater than or equal to 100
filtered_grouped = grouped[(grouped >= 100).all(axis=1)]

# Print the filtered DataFrame in markdown format
print(filtered_grouped.transpose().to_markdown())