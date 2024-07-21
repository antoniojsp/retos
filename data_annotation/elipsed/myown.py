import matplotlib.pyplot as plt
import matplotlib.patches as patches

width = 10
height = 5
angle = 0

fig, ax = plt.subplots()

ellipse = patches.Ellipse((0, 0), width, height, angle=angle, edgecolor='blue', facecolor='none')

ax.add_patch(ellipse)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

ax.set_aspect('equal')

ax.grid(True)

plt.show()