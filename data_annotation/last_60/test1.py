import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('last60.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Create a new column `Category Levels` by concatenating `Category Level 1`, `Category Level 2`, and `Category Level 3` columns separated by ' -> '.
df['Category Levels'] = df['Category Level 1'] + ' -> ' + df['Category Level 2'] + ' -> ' + df['Category Level 3']

# Print the unique values for `Category Levels`
print(df['Category Levels'].unique())