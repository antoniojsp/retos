# Import libraries
import matplotlib.pyplot as plt

# Country Names
countries = [
    "China", "India", "United States", "Indonesia", "Pakistan", "Brazil", "Nigeria",
    "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia", "Philippines", "Egypt",
    "Vietnam", "DR Congo", "Germany", "Iran", "Turkey", "Thailand", "United Kingdom",
    "France", "Italy", "Tanzania", "South Africa", "Myanmar", "South Korea", "Colombia",
    "Kenya", "Spain"
]

# Population in Millions
population_millions = [
    1444, 1400, 335, 279, 234, 215, 211, 171, 145, 130, 126, 115, 111, 106,
    99, 94, 84, 84, 84, 70, 67, 65, 60, 60, 60, 55, 52, 51, 50, 47
]

# Create a bar chart
plt.figure(figsize=(15, 8))  # Set the figure size
plt.bar(countries, population_millions)

# Set chart title and labels
plt.xlabel("Countries")
plt.ylabel("Population (Millions)")
plt.title("Population of the Most Populous Countries (2023)")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add data labels
for i, v in enumerate(population_millions):
    plt.text(i, v + 2, str(v), ha='center', va='bottom', fontsize=10)

# Show the chart
plt.tight_layout()
plt.show()