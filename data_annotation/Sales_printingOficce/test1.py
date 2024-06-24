import pandas as pd

# Load the CSV file to examine its contents and structure
file_path = 'Sales-PrintingOffice2023v1-Sheet1.csv'
sales_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
sales_data.head()

# Filter data for October and November based on 'Request date' and sum the 'Total Profit'

# Convert 'Request date' to datetime to extract month information, handling errors
sales_data['Request date'] = pd.to_datetime(sales_data['Request date'], errors='coerce')

# Filter the dataframe for October (10) and November (11) based on the 'Request date' month
oct_nov_data = sales_data[sales_data['Request date'].dt.month.isin([10, 11])]

# Sum up the 'Total Profit' for October and November
# The 'Total Profit' column contains dollar signs and commas, which need to be cleaned to convert to float
oct_nov_data['Total Profit Clean'] = oct_nov_data['Total Profit'].str.replace('[$,]', '', regex=True).astype(float)

total_sales_oct_nov = oct_nov_data['Total Profit Clean'].sum()

print(total_sales_oct_nov)