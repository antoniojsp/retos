import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df_alcohol_drug_abuse = pd.read_csv('Hospital_Survey_Data_Alcohol_Drug_Abuse 2.csv')

# Display the first 5 rows
print(df_alcohol_drug_abuse.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df_alcohol_drug_abuse.info())

# Rename `Unnamed: 12` to `Hospital Rating`
df_alcohol_drug_abuse = df_alcohol_drug_abuse.rename(columns={'Unnamed: 12': 'Hospital Rating'})

# Display the distinct values for `Hospital Rating`
print("Hospital Rating:", sorted(df_alcohol_drug_abuse['Hospital Rating'].unique()))

import numpy as np

# Get all unique non-numeric values from `Hospital Rating`
non_numeric_hospital_ratings = \
df_alcohol_drug_abuse[pd.to_numeric(df_alcohol_drug_abuse['Hospital Rating'], errors='coerce').isna()][
    'Hospital Rating'].unique()

if (len(non_numeric_hospital_ratings) > 20):
    # Sample 20 of them if there are too many unique values
    print(
        f"Non-numeric values in `Hospital Rating`: {np.random.choice(non_numeric_hospital_ratings, 20, replace=False)}")
else:
    # Otherwise print all unique non-numeric values from cost
    print(f"Non-numeric values in `Hospital Rating`: {non_numeric_hospital_ratings}")

# Rows where the value of `Hospital Rating` is equal to 'Hospital Rating'
df_to_drop = df_alcohol_drug_abuse[df_alcohol_drug_abuse['Hospital Rating'] == 'Hospital Rating']

# Drop rows
df_alcohol_drug_abuse = df_alcohol_drug_abuse.drop(df_to_drop.index)

# Filter rows with a hospital rating of 3 or more
df_filtered = df_alcohol_drug_abuse[
    df_alcohol_drug_abuse['Hospital Rating'].astype(float) >= 3.0
    ].copy()

# Sort the data by `Hospital Rating` in descending order
df_filtered.sort_values(
    by='Hospital Rating',
    ascending=False,
    inplace=True,
)

# Display the first 10 rows of the DataFrame
print(df_filtered.to_string())

