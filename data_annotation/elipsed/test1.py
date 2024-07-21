import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# set center as origin
center = (0, 0)

# set width as 20 and height as 10
width = 10
height = 5

# create ellipse object
e = matplotlib.patches.Ellipse(xy=center, width=width, height=height, angle=0, color='r')

# add object to plot
ax.add_patch(e)

# set limits
ax.set_xlim(-width, width)
ax.set_ylim(-height, height)

# set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')

# set title as 'Ellipse'
ax.set_title('Ellipse')

plt.show()
