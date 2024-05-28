import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv('hw_200.csv')

# Assuming the CSV has two columns named 'Column1' and 'Column2'
x_values = df['Index']
y_values = df['Height']

# Basic line plot
plt.plot(x_values, y_values)
plt.xlabel('Index')
plt.ylabel('Height')
plt.title('Plot of CSV Data')
plt.show()