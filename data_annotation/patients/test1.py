import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('patient_list-_patient_list.csv')

# # Display the first 5 rows
# print(df.head())
#
# # Print the column names and their data types
# print(df.info())

from pandas.api.types import CategoricalDtype

# Convert `payment_method` column to categorical
payment_method_categories = ['cash', 'card', 'transfer']
payment_method_dtype = CategoricalDtype(categories=payment_method_categories, ordered=True)
df['payment_method'] = df['payment_method'].astype(payment_method_dtype)

# Count the occurrences of each payment method
payment_method_counts = df['payment_method'].value_counts().to_markdown()
print(f"Number of rows for each payment method:\n{payment_method_counts}")


# Filter the DataFrame to only include rows where payment_method is 'cash'
cash_patients = df[df['payment_method'] == 'cash']

# Filter the DataFrame to only include rows where release_date is 'in progress'
in_progress_cash_patients = cash_patients[cash_patients['release_date'] == 'in progress']

# Display the first 5 rows
print(in_progress_cash_patients.head())

# Print the column names and their data types
print(in_progress_cash_patients.info())