import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("DATA_ECOM_VAS_v1-.xlsx-Grossreport.csv")

# Display the first 5 rows and all columns
print(df.head())

# Display column names and their types
print(df.info())
