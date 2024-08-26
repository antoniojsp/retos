import trimesh
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the STL file
mesh = trimesh.load('file.stl')

# Set up the figure and axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')


# Function to update the plot with the rotating mesh
def update(frame):
    # Rotate the mesh around the z-axis
    theta = np.radians(frame)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    new_vertices = np.dot(mesh.vertices, R.T)
    new_mesh = trimesh.Trimesh(vertices=new_vertices, faces=mesh.faces)

    # Clear the previous plot
    ax.cla()

    # Plot the rotated mesh
    new_mesh.plot(ax=ax)

    # Set the axes limits and labels
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Spinning STL Object')

    return ax,


# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 60), interval=50, blit=True)

# Display the animation
plt.show()