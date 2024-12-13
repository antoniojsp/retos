import pandas as pd

# Sample DataFrame for demonstration
data = {
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 'Around the Horn'],
    'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno', 'Thomas Hardy'],
    'Country': ['Germany', 'Mexico', 'Mexico', 'UK']
}

df = pd.DataFrame(data)

# Display the DataFrame before deletion
print("DataFrame before deletion:")
print(df)

# Delete rows where CustomerName is 'Alfreds Futterkiste'
df = df[df['CustomerName'] != 'Alfreds Futterkiste']

# Display the DataFrame after deletion
print("\nDataFrame after deletion:")
print(df)