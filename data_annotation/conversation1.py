import matplotlib.pyplot as plt
import numpy as np

# Data points (mimicking the image)
data = {
    "Base": [(1, 65), (10, 88), (1000, 110)],
    "Large": [(1, 78), (10, 108), (1000, 122)],
    "Huge": [(1, 92), (10, 120), (1000, 145)]
}

# Plotting
plt.figure(figsize=(8, 5))
for model_name, points in data.items():
    x, y = zip(*points)  # Unpack x and y coordinates
    plt.plot(x, y, marker='o' if model_name == "Huge" else 'x', linestyle='-', label=model_name)

# Customization
plt.xscale('log')  # Logarithmic scale for x-axis
plt.xlabel('million images in pre-training')
plt.ylabel('CIDEr')
plt.grid(True)
plt.legend()
plt.title('CIDEr vs. Pre-Training Data Size')

plt.show()

#
#
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Data for plotting
# x = [5, 12, 100, 1000]
# base_y = [70, 80, 100, 115]
# large_y = [80, 110, 115, 125]
# huge_y = [95, 120, 130, 145]
#
# # Create figure and axis
# fig, ax = plt.subplots()
#
# # Plot the curves
# ax.plot(x, base_y, marker='*', markersize=10, label='Base')
# ax.plot(x, large_y, marker='x', markersize=10, label='Large')
# ax.plot(x, huge_y, marker='o', markersize=10, label='Huge')
#
# # Set x and y labels
# ax.set_xlabel('million images in pre-training')
# ax.set_ylabel('CIDEr')
#
# # Set x-axis to log scale
# ax.set_xscale('log')
#
# # Add grid
# ax.grid(True)
#
# # Add legend
# ax.legend()
#
# # Show the plot
# plt.show()