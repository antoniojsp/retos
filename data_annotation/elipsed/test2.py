import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# set center as origin
center = (0, 0)

# set width as 2*horizontal radius
width = 2 * 10

# set height as 2*vertical radius
height = 2 * 5

# create ellipse object
e = matplotlib.patches.Ellipse(xy=center, width=width, height=height, angle=0, color='r')

# add object to plot
ax.add_patch(e)

# set limits
ax.set_xlim(-width + center[0], width + center[0])
ax.set_ylim(-height + center[1], height + center[1])

# set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')

# set title as 'Ellipse'
ax.set_title('Ellipse')

plt.show()