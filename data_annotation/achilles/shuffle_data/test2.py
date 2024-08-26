import pandas as pd

# Sample DataFrame
data = {'column1': [1, 2, 3, 4, 5],
        'column2': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# Shuffle the DataFrame
df_shuffled = df.sample(frac=1, random_state=42)  # Set a random seed for reproducibility

print(df_shuffled)