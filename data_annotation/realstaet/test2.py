import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame using 'latin-1' encoding
# df = pd.read_csv('Real Estate Mumbai Database - Rgdcvvvh.csv', encoding='latin-1')
# It seems there was a UnicodeDecodeError. Let's try reading the file with a different encoding.
# Attempt to load the CSV file again using the ISO-8859-1 encoding

data = pd.read_csv("Real Estate Mumbai Database - Rgdcvvvh.csv", encoding='ISO-8859-1')

# Display the first few rows of the dataframe to understand its structure and the specific column
data.head()
# Split the "AMOUNT IN (INR)" into "THOUSANDS" and "HUNDREDS"
data['THOUSANDS'] = (data['AMOUNT IN (INR)'] // 1000) * 1000
data['HUNDREDS'] = data['AMOUNT IN (INR)'] % 1000

# Display the first few rows to verify the new columns
print(data.head())