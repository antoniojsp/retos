# Let's start by loading the uploaded CSV file to inspect its contents and find the 'Total Sales' value for the specified campaign.
import pandas as pd

# Load the CSV file
file_path = 'paid-ads-top-campaigns-table_2023-11-30_2023-12-29.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(df.to_string())