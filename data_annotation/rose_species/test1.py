

# Import libraries
import pandas as pd

# Create a list of data
data = [
    [1, 5.1, 3.5, 1.4, 0.2, "Setosa"],
    [2, 4.9, 3.0, 1.4, 0.2, "Setosa"],
    [3, 4.7, 3.2, 1.3, 0.2, "Setosa"],
    [4, 4.6, 3.1, 1.5, 0.2, "Setosa"],
    [5, 5.0, 3.6, 1.4, 0.2, "Setosa"],
    [6, 5.4, 3.9, 1.7, 0.4, "Setosa"],
    [7, 4.6, 3.4, 1.4, 0.3, "Versicolor"],
    [8, 5.0, 3.4, 1.5, 0.2, "Versicolor"],
    [9, 4.4, 2.9, 1.4, 0.2, "Versicolor"],
    [10, 4.9, 3.1, 1.5, 0.1, "Versicolor"],
    [11, 5.4, 3.7, 1.5, 0.2, "Versicolor"],
]

# Create a DataFrame
df = pd.DataFrame(data, columns=["flower_id", "sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

# Calculate the range of sepal lengths for each species
sepal_length_range_by_species = df.groupby("species")["sepal_length"].max() - df.groupby("species")[
    "sepal_length"].min()

# Print the results
print(sepal_length_range_by_species)