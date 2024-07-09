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

# Correctly grouping and aggregating the data
grouped = (
    df.groupby(['JOB DESC', 'CONCEPT'], as_index=False)['TOTAL']
    .sum()
)

# Pivot the data with 'JOB DESC' as rows and 'CONCEPT' as columns
pivot_table = grouped.pivot(index='JOB DESC', columns='CONCEPT', values='TOTAL').reset_index()

# Removing rows and columns with all NaN values (which can occur if all values are below the threshold)
pivot_table_cleaned = pivot_table.dropna(how='all', axis=0).dropna(how='all', axis=1)

# # Apply a mask to remove values less than 100
# filtered_table = pivot_table_cleaned.mask(pivot_table_cleaned < 100)
#
# print(filtered_table.head())

# Select only numeric columns for comparison
numeric_cols = pivot_table.select_dtypes(include=['number']).columns

# Apply the mask for values less than 100 only on numeric columns
pivot_table[numeric_cols] = pivot_table[numeric_cols].mask(pivot_table[numeric_cols] < 100)

# Display the first few rows of the adjusted table
print(pivot_table.head())
