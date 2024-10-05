import pandas as pd

# Load data
df = pd.read_csv("log.csv")
# Rows
# print("Number of rows and columns in the data:", df.shape)
# # Columns
# print("Columns of the data are:", len(df.columns))
# # Column names
# print("Column names of the data are:", df.columns)
# # Column dtypes
# print("Datatypes of the columns are:", df.dtypes)
# # Sample of data
# print("Data sample from file:")

# print(df.info())
# print(df.to_string())
# print(df["Details"].to_string())
# print(df[df["Details"] == "James City Supplies"].to_string())
print(df[df["Details"] == "James City Supplies"]["Cost"])

# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Load data
# df = pd.read_csv("log.csv")
#
# # Convert 'Cost' column to numeric
# df['Cost'] = pd.to_numeric(df['Cost'].str.replace('$', '').str.replace(',', ''))
#
# # Calculate total number of payments
# total_payments = df.shape[0]
#
# # Calculate total amount paid to James City Supplies
# jcs_payments = df[df['Details'] == 'James City Supplies']
# total_jcs_amount = jcs_payments['Cost'].sum()
#
# # Calculate average amount paid per invoice for other material expenses
# other_materials = df[(df['Expense Type'] == 'Materials') & (df['Details'] != 'James City Supplies')]
# average_other_materials = other_materials['Cost'].mean()
#
# # Calculate average amount paid per invoice to James City Supplies
# average_jcs = jcs_payments['Cost'].mean()
#
# # Print results
# print(f'Total number of payments: {total_payments}')
# print(f'Total amount paid to James City Supplies: ${total_jcs_amount:.2f}')
# print(f'Average amount paid per invoice for other material expenses: ${average_other_materials:.2f}')
# print(f'Average amount paid per invoice to James City Supplies: ${average_jcs:.2f}')
#
# # Plot bar graph
# plt.bar(['Other Materials', 'James City Supplies'], [average_other_materials, average_jcs])
# plt.xlabel('Expense Type')
# plt.ylabel('Average Amount Paid per Invoice')
# plt.title('Average Amount Paid per Invoice by Expense Type')
# plt.show()