import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# Load the CSV file
septicemia_data = pd.read_csv('Hospital_Survey_Data_Speticemia.csv', skiprows = [0])

# Load the Excel file
alcohol_drug_abuse_data = pd.read_excel('Hospital_Survey_Data_Alcohol_Drug_Abuse.xlsx', skiprows = [0])

# Check the first few rows of each dataframe to understand the structure and the column names
# Convert 'Provider Zip Code' to string for concatenation
septicemia_data['Provider Zip Code'] = septicemia_data['Provider Zip Code'].astype(str)
alcohol_drug_abuse_data['Provider Zip Code'] = alcohol_drug_abuse_data['Provider Zip Code'].astype(str)

# Recreate the 'Location' column with corrected data types
septicemia_data['Location'] = septicemia_data['Provider City'] + ', ' + septicemia_data['Provider State'] + ' ' + \
                              septicemia_data['Provider Zip Code']
alcohol_drug_abuse_data['Location'] = alcohol_drug_abuse_data['Provider City'] + ', ' + alcohol_drug_abuse_data[
    'Provider State'] + ' ' + alcohol_drug_abuse_data['Provider Zip Code']

# Displaying the first few rows of each dataframe to verify the new column
septicemia_data[['Provider City', 'Provider State', 'Provider Zip Code', 'Location']].head(), alcohol_drug_abuse_data[
    ['Provider City', 'Provider State', 'Provider Zip Code', 'Location']].head()
print(septicemia_data)