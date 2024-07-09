import pandas as pd

# Load the CSV file
file_path = 'sales_memos.csv'
sales_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
sales_data.head()

# Filter the data for EDAFLORS
edaflors_data = sales_data[sales_data['Company'] == 'EDAFLORS']

# Clean and convert the 'Commission' column to a uniform numeric format
def convert_commission(commission):
    # Remove currency symbols and convert to float
    commission = commission.replace('Eur', '').replace('u$s', '').replace('.', '').replace(',', '.')
    return float(commission)

edaflors_data['Commission'] = edaflors_data['Commission'].apply(convert_commission)

# Convert 'Date' column to datetime format
edaflors_data['Date'] = pd.to_datetime(edaflors_data['Date'], format='%d/%m/%Y')

# Group by month and year, then sum the commissions
edaflors_monthly_commission = edaflors_data.groupby(edaflors_data['Date'].dt.to_period('M'))['Commission'].sum().reset_index()

# Display the monthly commission data
# import ace_tools as tools; tools.display_dataframe_to_user(name="EDAFLORS Monthly Commission", dataframe=edaflors_monthly_commission)

print(edaflors_monthly_commission)