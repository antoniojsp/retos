import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', None)  # No limit on the width
pd.set_option('display.max_colwidth', None)  # Display full column width

# Read the CSV file into a DataFrame
df = pd.read_csv('patient_list-_patient_list.csv')

# Display the first 5 rows
# print(df.head())

# Print the column names and their data types

from pandas.api.types import CategoricalDtype
# Convert `payment_method` column to categorical
# payment_method_categories = ['cash', 'card', 'transfer']
# payment_method_dtype = CategoricalDtype(categories=payment_method_categories, ordered=True)
# df['payment_method'] = df['payment_method'].astype(payment_method_dtype)
# payment_method_counts = df['payment_method'].value_counts().to_markdown()
df_cash = df[(df["payment_method"] == "cash") & (df["release_date"] == "in progress")]
print(df_cash)
