import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 28],
        'score': [8.5, 9.2, 7.8]}
df = pd.DataFrame(data)

types = df.dtypes
print(types)
