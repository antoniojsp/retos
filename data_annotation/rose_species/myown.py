import pandas as pd

# Creating the initial DataFrame
data = {
    "sepal_length": [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4],
    "species": ["Setosa", "Setosa", "Setosa", "Setosa", "Setosa", "Setosa", "Versicolor", "Versicolor", "Versicolor", "Versicolor", "Versicolor"]
}

df = pd.DataFrame(data)

range_df = df.groupby("species")["sepal_length"].apply(lambda x: x.max() - x.min())

# Displaying the result
print(range_df)