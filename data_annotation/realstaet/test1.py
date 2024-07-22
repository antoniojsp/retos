import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame using 'latin-1' encoding
df = pd.read_csv('Real Estate Mumbai Database - Rgdcvvvh.csv', encoding='latin-1')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Extract thousands and hundreds place values
df['THOUSANDS'] = df['AMOUNT IN (INR)'] // 1000
df['HUNDREDS'] = (df['AMOUNT IN (INR)'] % 1000) // 100

# Print the first 5 rows of the updated dataframe
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))