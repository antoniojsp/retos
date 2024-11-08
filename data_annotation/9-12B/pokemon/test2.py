import pandas as pd

# Load the data from the uploaded file
file_path = 'info.json'

# Load the JSON data from the file
pokemon_data = pd.read_json(file_path)

# Display the timers few rows of the dataframe and its columns to understand its structure
print(pokemon_data.head(), pokemon_data.columns)

# Create a new column to count the number of types each Pokémon has
pokemon_data['type_count'] = pokemon_data['type'].apply(len)
print(pokemon_data.to_string())
# Calculate average attack for Pokémon with one type and two types
average_attack_one_type = pokemon_data[pokemon_data['type_count'] == 1]['attack'].mean()
average_attack_two_types = pokemon_data[pokemon_data['type_count'] == 2]['attack'].mean()

print(average_attack_one_type -  average_attack_two_types)

