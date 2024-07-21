import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('last60.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Combine the three category columns into a single column
df['Category Levels'] = df['Category Level 1'] + ' > ' + df['Category Level 2'] + ' > ' + df['Category Level 3']

# Write the updated DataFrame to a new csv file
df.to_csv('last60_with_combined_categories.csv', index=False)