import pandas as pd

# Create a DataFrame from the provided data
data = {
    'flower_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4],
    'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7],
    'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5, 1.5],
    'petal_width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 0.2],
    'species': ['Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Setosa', 'Versicolor', 'Versicolor', 'Versicolor', 'Versicolor', 'Versicolor']
}

df = pd.DataFrame(data)

# Calculate the range of sepal lengths for each species
sepal_length_range_by_species = df.groupby('species')['sepal_length'].agg(max=pd.NamedAgg(column='sepal_length', aggfunc='max'), min=pd.NamedAgg(column='sepal_length', aggfunc='min'))

# Print the results
print(sepal_length_range_by_species)