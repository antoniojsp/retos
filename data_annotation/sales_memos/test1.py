import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('sales_memos.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Filter data on `Company` for the value 'EDAFLORS'
df_filtered = df[df['Company'] == 'EDAFLORS'].copy()

# Remove 'Eur', 'u$s', '.' and ',' from `Commission` column
df_filtered['Commission'] = df_filtered['Commission'].astype(str).str.replace('Eur', '', ).str.replace('u\$s',
                                                                                                       '', ).str.replace(
    '.', '', ).str.replace(',', '.', )

# Convert the `Commission` column to numeric
df_filtered['Commission'] = pd.to_numeric(df_filtered['Commission'], errors='coerce')

# Convert `Date` column to datetime
df_filtered['Date'] = pd.to_datetime(df_filtered['Date'], format='%d/%m/%Y', errors='coerce')

# Extract month from `Date` column
df_filtered['Month'] = df_filtered['Date'].dt.month

# Group data on month and sum the `Commission` column
df_grouped = df_filtered.groupby('Month')['Commission'].sum().reset_index()

# Rename `Commission` column to 'Total Commission'
df_grouped = df_grouped.rename(columns={'Commission': 'Total Commission'})

# Sort grouped data on month in ascending order
df_grouped = df_grouped.sort_values('Month')

# Display the data
print(df_grouped.to_markdown(index=False, numalign="left", stralign="left"))
