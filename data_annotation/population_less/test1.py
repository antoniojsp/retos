import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV files into Pandas Dataframes
df_ny = pd.read_csv('population_ny.csv')
df_ma = pd.read_csv('population_ma.csv')
df_ca = pd.read_csv('population_ca.csv')

# Display the first 5 rows of each DataFrame
print("First 5 rows of the New York DataFrame:")
print(df_ny.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of the Massachusetts DataFrame:")
print(df_ma.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of the California DataFrame:")
print(df_ca.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types for each DataFrame
print("\nColumn names and their data types for the New York DataFrame:")
print(df_ny.info())

print("\nColumn names and their data types for the Massachusetts DataFrame:")
print(df_ma.info())

print("\nColumn names and their data types for the California DataFrame:")
print(df_ca.info())

# Remove ',' from `Population` column and convert it to numeric for each DataFrame
df_ny['Population'] = df_ny['Population'].astype(str).str.replace(',', '', regex=False)
df_ny['Population'] = pd.to_numeric(df_ny['Population'])

df_ma['Population'] = df_ma['Population'].astype(str).str.replace(',', '', regex=False)
df_ma['Population'] = pd.to_numeric(df_ma['Population'])

df_ca['Population'] = df_ca['Population'].astype(str).str.replace(',', '', regex=False)
df_ca['Population'] = pd.to_numeric(df_ca['Population'])

# Filter the DataFrames to only contain rows where `Population` is greater than or equal to 10000
df_ny_filtered = df_ny[df_ny['Population'] >= 10000]
df_ma_filtered = df_ma[df_ma['Population'] >= 10000]
df_ca_filtered = df_ca[df_ca['Population'] >= 10000]

# Display the first 5 rows of each of the filtered DataFrames
print("First 5 rows of the filtered New York DataFrame:")
print(df_ny_filtered.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of the filtered Massachusetts DataFrame:")
print(df_ma_filtered.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of the filtered California DataFrame:")
print(df_ca_filtered.head().to_markdown(index=False, numalign="left", stralign="left"))
