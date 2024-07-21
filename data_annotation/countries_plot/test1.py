import matplotlib.pyplot as plt

# Create a list of country names
countries = [
    "China", "India", "United States", "Indonesia", "Pakistan", "Brazil",
    "Nigeria", "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia",
    "Philippines", "Egypt", "Vietnam", "DR Congo", "Germany", "Iran",
    "Turkey", "Thailand", "United Kingdom", "France", "Italy", "Tanzania",
    "South Africa", "Myanmar", "South Korea", "Colombia", "Kenya", "Spain"
]

# Create a list of population values in millions
populations = [1444, 1400, 335, 279, 234, 215, 211, 171, 145, 130, 126, 115,
               111, 106, 99, 94, 84, 84, 84, 70, 67, 65, 60, 60, 60, 55, 52,
               51, 50, 47]

# Create a bar chart
plt.figure(figsize=(12, 8))  # Set the figure size
plt.barh(countries, populations, color='skyblue')  # Create the bar chart
plt.xlabel('Population (millions)')  # Add a label for the x-axis
plt.ylabel('Country')  # Add a label for the y-axis
plt.title('Population of the Most Populous Countries (2023)')  # Add a title for the chart
plt.gca().invert_yaxis()  # Invert the y-axis to display the most populous country at the top

# Display the bar chart
plt.tight_layout()
plt.show()