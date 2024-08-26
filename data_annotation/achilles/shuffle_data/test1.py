import pandas as pd

data = {'column1': [1, 2, 3, 4, 5],
        'column2': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)




# Assuming you have a DataFrame named 'df'
shuffled_df = df.sample(frac=1)
print(shuffled_df)