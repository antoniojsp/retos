import matplotlib.pyplot as plt

# Budget allocation for clothing categories
clothing_categories = ["Tops", "Bottoms", "Dresses", "Shoes", "Outerwear", "Accessories"]
budget_allocation = [30, 25, 15, 15, 10, 5]  # Percentages

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(budget_allocation, labels=clothing_categories, autopct="%1.1f%%", startangle=140)
plt.title("Clothing Budget Allocation for 2024")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.show()