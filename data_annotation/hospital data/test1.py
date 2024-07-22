import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV files into Pandas Dataframes
df_alcohol_drug_abuse = pd.read_csv('Hospital_Survey_Data_Alcohol_Drug_Abuse 2.csv', skiprows=1)
df_speticemia = pd.read_csv('Hospital_Survey_Data_Speticemia.csv', skiprows=1)

# Display the first 5 rows of each DataFrame
print("First 5 rows of Alcohol_Drug_Abuse DataFrame:")
print(df_alcohol_drug_abuse.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of Speticemia DataFrame:")
print(df_speticemia.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types for each DataFrame
print("\nAlcohol_Drug_Abuse DataFrame Information:")
print(df_alcohol_drug_abuse.info())

print("\nSpeticemia DataFrame Information:")
print(df_speticemia.info())

# Create the `Location` column in `df_alcohol_drug_abuse`
df_alcohol_drug_abuse['Location'] = df_alcohol_drug_abuse['Provider City'] + ', ' + df_alcohol_drug_abuse['Provider State'] + ', ' + df_alcohol_drug_abuse['Provider Zip Code'].astype(str)

# Create the `Location` column in `df_speticemia`
df_speticemia['Location'] = df_speticemia['Provider City'] + ', ' + df_speticemia['Provider State'] + ', ' + df_speticemia['Provider Zip Code'].astype(str)

# Display the first 5 rows of each DataFrame
print("First 5 rows of Alcohol_Drug_Abuse DataFrame:")
print(df_alcohol_drug_abuse.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nFirst 5 rows of Speticemia DataFrame:")
print(df_speticemia.head().to_markdown(index=False, numalign="left", stralign="left"))