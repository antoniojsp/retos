import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('trapiche_ingenio_nv.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Calculate the total `Azucar`
total_azucar = df['Azucar'].sum()

# Print the total `Azucar`
print(f"The total 'Azucar' produced is: {total_azucar}")