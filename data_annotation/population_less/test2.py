import pandas as pd

# Load the data from the uploaded CSV files
ny_data = pd.read_csv('population_ny.csv')
ma_data = pd.read_csv('population_ma.csv')
ca_data = pd.read_csv('population_ca.csv')

# Convert 'Population' columns to numeric values (integers) before filtering
ny_data['Population'] = pd.to_numeric(ny_data['Population'], errors='coerce')
ma_data['Population'] = pd.to_numeric(ma_data['Population'], errors='coerce')
ca_data['Population'] = pd.to_numeric(ca_data['Population'], errors='coerce')

# Filter out cities with a population less than 10000 again
ny_filtered = ny_data[ny_data['Population'] <= 250000]
ma_filtered = ma_data[ma_data['Population'] <= 10000]
ca_filtered = ca_data[ca_data['Population'] <= 10000]

# Save the filtered data to new CSV files again
ny_filtered.to_csv('population_ny_filtered.csv', index=False)
ma_filtered.to_csv('population_ma_filtered.csv', index=False)
ca_filtered.to_csv('population_ca_filtered.csv', index=False)
