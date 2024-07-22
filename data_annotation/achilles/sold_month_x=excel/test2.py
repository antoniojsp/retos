import pandas as pd

# Load the Excel file
file_path = "SOLDFOOD2023 - Winter.xlsx"
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()

# Extracting relevant columns and data
relevant_data = data.iloc[3:, [2, 4]]  # Selecting rows and columns relevant to 'GROUP' and 'QUANTITY'
relevant_data.columns = ['Group', 'Quantity']  # Renaming columns for clarity

# Convert 'Quantity' to numeric, errors='coerce' will turn non-numeric values to NaN
relevant_data['Quantity'] = pd.to_numeric(relevant_data['Quantity'], errors='coerce')

# Grouping by 'Group' and calculating the average quantity sold
average_quantity_sold = relevant_data.groupby('Group')['Quantity'].mean()

print(average_quantity_sold)