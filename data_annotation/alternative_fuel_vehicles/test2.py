import pandas as pd

# Load the CSV file to understand its structure and contents
file_path = 'Alternative Fuel Vehicles US.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
df.head()

# Filter the dataframe for vehicles that are either sedans or SUVs with AWD
awd_vehicles = df[(df['Drivetrain'] == 'AWD') & (df['Category'].str.contains('Sedan|SUV'))]

# Sort the filtered vehicles by their combined alternative fuel economy (if available) and then by conventional fuel economy
awd_vehicles_sorted = awd_vehicles.sort_values(by=['Alternative Fuel Economy Combined', 'Conventional Fuel Economy Combined'], ascending=False)

# Select relevant columns to simplify the output
relevant_columns = ['Category', 'Model', 'Model Year', 'Manufacturer', 'Fuel', 'All-Electric Range', 'PHEV Total Range', 'Alternative Fuel Economy Combined', 'Conventional Fuel Economy Combined', 'Drivetrain']
awd_vehicles_sorted_filtered = awd_vehicles_sorted[relevant_columns]

# Display the top 10 vehicles based on the sorting criteria
print(awd_vehicles_sorted_filtered.head(10))