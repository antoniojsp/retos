import pandas as pd

# The first row is actually the header, so we'll reload the dataframe with the correct header
drug_abuse_data = pd.read_excel("Hospital_Survey_Data_Alcohol_Drug_Abuse.xlsx", header=1)

# Now, filter the data for providers with a hospital rating of 3 or more
filtered_drug_abuse_data = drug_abuse_data[drug_abuse_data["Hospital Rating"] >= 3]

# Display the filtered data
print(filtered_drug_abuse_data.to_string())