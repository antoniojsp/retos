import matplotlib.pyplot as plt

# Data
x = [0.166154, 6.997652, 8.343716, 0.745566, 9.349767, 9.688314, 8.317796, 0.684721, 2.307429, 7.398172]
y = [51.532447, 39.946623, 80.374628, 74.501008, 25.852622, 63.375963, 38.437411, -0.204118, 33.641793, 58.106066]

# Plotting the points
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue')
plt.title('Scatter Plot of Given Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()