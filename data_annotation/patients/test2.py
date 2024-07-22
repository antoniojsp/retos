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

# Filter for patients who pay with cash and are at the beginning of treatment
filtered_df = df[(df['payment_method'] == 'cash') & (df['release_date'] == 'in progress')]

# Display the filtered DataFrame
if not filtered_df.empty:
    print("Patients at the beginning of treatment and paying with cash:")
    print(filtered_df[['name', 'date_of_birth', 'payment_method', 'beginning_of_traetment']].to_markdown(index=False))
else:
    print("There are no patients at the beginning of treatment who pay with cash.")

