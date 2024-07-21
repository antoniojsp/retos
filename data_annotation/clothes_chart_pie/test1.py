# Import libraries
import matplotlib.pyplot as plt

# Define data
categories = ["Shirts", "Pants", "Shoes", "Coats", "Accessories"]
budget = [200, 150, 100, 75, 50]  # Replace with your actual budget data

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(budget, labels=categories, autopct="%1.1f%%", startangle=90)
plt.title("2024 Clothing Budget")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display pie chart
plt.show()
