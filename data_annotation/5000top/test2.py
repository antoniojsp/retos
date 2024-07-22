import pandas as pd

# Load the data from the uploaded file
file_path = 'population_and_age.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
print(data.head())

# Calculate the total population and the weighted average age
total_population = data['Population (Million)'].sum()
weighted_average_age = (data['Average Age (Years)'] * data['Population (Million)']).sum() / total_population

print(total_population, weighted_average_age)
