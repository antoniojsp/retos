import pandas as pd

# Sample DataFrame (replace with your actual data)
data = {'CustomerID': [1, 2, 3, 4, 5],
        'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 'Around the Horn', 'Bérgsonn Merchants'],
        'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno', 'Thomas Hardy', 'Christina Berglund'],
        'City': ['Berlin', 'México D.F.', 'México D.F.', 'London', 'Luleå'],
        'Country': ['Germany', 'Mexico', 'Mexico', 'UK', 'Sweden']}
customers = pd.DataFrame(data)

# Equivalent of the SQL DELETE statement
# customers = customers[customers['CustomerName'] != 'Alx/

# Print the updated DataFrame
print(customers)


# Another way using .drop() with index
data = {'CustomerID': [1, 2, 3, 4, 5],
        'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 'Around the Horn', 'Bérgsonn Merchants'],
        'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno', 'Thomas Hardy', 'Christina Berglund'],
        'City': ['Berlin', 'México D.F.', 'México D.F.', 'London', 'Luleå'],
        'Country': ['Germany', 'Mexico', 'Mexico', 'UK', 'Sweden']}
customers = pd.DataFrame(data)

indices_to_drop = customers[customers['CustomerName'] == 'Alfreds Futterkiste'].index
customers = customers.drop(indices_to_drop)

print(customers)

# If you want to modify the DataFrame in place (like DELETE in SQL)
data = {'CustomerID': [1, 2, 3, 4, 5],
        'CustomerName': ['Alfreds Futterkiste', 'Ana Trujillo Emparedados y helados', 'Antonio Moreno Taquería', 'Around the Horn', 'Bérgsonn Merchants'],
        'ContactName': ['Maria Anders', 'Ana Trujillo', 'Antonio Moreno', 'Thomas Hardy', 'Christina Berglund'],
        'City': ['Berlin', 'México D.F.', 'México D.F.', 'London', 'Luleå'],
        'Country': ['Germany', 'Mexico', 'Mexico', 'UK', 'Sweden']}
customers = pd.DataFrame(data)

customers.drop(customers[customers['CustomerName'] == 'Alfreds Futterkiste'].index, inplace=True)
print(customers)