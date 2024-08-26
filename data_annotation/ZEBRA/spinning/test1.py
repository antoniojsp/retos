import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from trimesh import Trimesh

# Load STL file
mesh = Trimesh(filename="test.stl")

fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2), zlim=(-2, 2))
ax.set_aspect('equal')


def init():
    ax.add_artist(mesh)
    return [mesh]


def animate(i):
    mesh.apply_transform(mesh.visual.transform(matrix=[[np.cos(i / 60), -np.sin(i / 60), 0],
                                                       [np.sin(i / 60), np.cos(i / 60), 0],
                                                       [0, 0, 1]]))
    return [mesh]


# Creating animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)
plt.show()
