import pandas as pd

# Create a sample DataFrame
data = {'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)
print(df)
# List of values to filter out
values_to_remove = [2, 4]

# Filter the DataFrame
filtered_df = df[~df['Column1'].isin(values_to_remove)]

print(filtered_df)