import json

# Load the json file
# with open("info.json", 'r') as f:
#     data = json.load(f)
#
#     # Print the data
#     print(data)

import json
import pandas as pd

# Load the json file
with open("info.json", 'r') as f:
    data = json.load(f)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Calculate the difference in attack for Pokemon with 1 type vs 2 types
df['type_count'] = df['type'].apply(len)
df['attack_diff'] = df['attack'] - df.groupby('type_count')['attack'].transform('mean')

# Print the result
print(df[['name', 'type', 'attack', 'type_count', 'attack_diff']].to_string(index=False))

