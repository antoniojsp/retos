import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Chainmaille_by_Yael_– Customer_Data_(2023).csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Calculate the number of missing values for each column
print("Missing values per column:")
print(df.isnull().sum().to_markdown(numalign="left", stralign="left"))

# Calculate the number of unique values for each column
print("Unique values per column:")
print(df.nunique().to_markdown(numalign="left", stralign="left"))

# Calculate descriptive statistics for all numeric columns
print("Descriptive statistics for numeric columns:")
print(df.describe().to_markdown(numalign="left", stralign="left"))
