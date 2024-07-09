import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv('Retail Store Performance and Capacity Metrics - EXO2E Crypto - cccvvv.tsv', delimiter='\t')
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Rename the columns `Installed Capacity 20` and `Installed Capacity 30` to `installed_20` and `installed_30` respectively
df = df.rename(columns={'Installed Capacity 20': 'installed_20', 'Installed Capacity 30': 'installed_30'})

# Insert a new column to the right of `installed_30` called `Installed Capacity Difference` that is the difference between `installed_20` and `installed_30`
df.insert(df.columns.get_loc('installed_30') + 1, 'Installed Capacity Difference',
          df['installed_20'] - df['installed_30'])

# Write the dataframe to a csv file called "retail_store_performance_installed_difference.csv"
df.to_csv('retail_store_performance_installed_difference2.csv', index=False)
print(df.head())