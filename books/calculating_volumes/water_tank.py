from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def prism(baseAxes:dict = {"x":0, "y":0, "z":0}, axes:dict = {"x":1, "y":1, "z":1}, multiplier:int = 1) -> list:

    axes = {i:axes[i] * multiplier for i in axes.keys()}

    axes = {i:axes[i] + baseAxes[i] for i in axes.keys()}

    vertices = [
        [baseAxes["x"],     baseAxes["y"],      baseAxes["z"]],  # Vertex 0
        [axes["x"],         baseAxes["y"],      baseAxes["z"]],  # Vertex 1
        [axes["x"],         axes["y"],          baseAxes["z"]],  # Vertex 2
        [baseAxes["x"],     axes["y"],          baseAxes["z"]],  # Vertex 3
        [baseAxes["x"],     baseAxes["y"],          axes["z"]],  # Vertex 4
        [axes["x"],         baseAxes["y"],          axes["z"]],  # Vertex 5
        [axes["x"],         axes["y"],              axes["z"]],  # Vertex 6
        [baseAxes["x"],     axes["y"],              axes["z"]]   # Vertex 7
    ]
    print(axes)

    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],  # Face bottom
        [vertices[j] for j in [4, 5, 6, 7]],  # Face top
        [vertices[j] for j in [0, 1, 5, 4]],  # Face front
        [vertices[j] for j in [1, 2, 6, 5]],  # Face right
        [vertices[j] for j in [2, 3, 7, 6]],  # Face back
        [vertices[j] for j in [3, 0, 4, 7]]   # Face left
    ]

    return {"faces":faces, "axes":axes, "volume": (np.prod(list(axes.values())) * 1000)}


t = 2

# Define the vertices of the cube
vertices = [
    [0, 0, 0],  # Vertex 0
    [1, 0, 0],  # Vertex 1
    [1, 1, 0],  # Vertex 2
    [0, 1, 0],  # Vertex 3
    [0, 0, 1],  # Vertex 4
    [1, 0, 1],  # Vertex 5
    [1, 1, 1],  # Vertex 6
    [0, 1, 1]   # Vertex 7
]

# Define the vertices that compose the six faces of the cube
faces = [
    [vertices[j] for j in [0, 1, 2, 3]],  # Face bottom
    [vertices[j] for j in [4, 5, 6, 7]],  # Face top
    [vertices[j] for j in [0, 1, 5, 4]],  # Face front
    [vertices[j] for j in [1, 2, 6, 5]],  # Face right
    [vertices[j] for j in [2, 3, 7, 6]],  # Face back
    [vertices[j] for j in [3, 0, 4, 7]]   # Face left
]


prism1 = prism(axes={"x": 2, "y": 2, "z": 1}, multiplier=1)


df = pd.DataFrame(prism1["faces"], columns=['Ponto 1', 'Ponto 2', 'Ponto 3', 'Ponto 4'], index=['Face inferior', 'Face superior', 'Face frontal', 'Face direita', 'Face tras', 'Face esquerda'])

print(df)

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a 3D polygon collection and add it to the axes
ax.add_collection3d(Poly3DCollection(prism1["faces"], facecolors='cyan', linewidths=1, edgecolors='black', alpha=.25))
ax.text((prism1["axes"]["x"]/2), (prism1["axes"]["y"]/2), (prism1["axes"]["z"] + 1), str(f"{prism1['volume']}L"), color='black', fontsize=24, ha='center', va='center',  bbox=dict(facecolor='red', alpha=0.5))

point1 = [0, 0, -0.1]
point2 = [2, 0, -0.1]

ax.plot([point1[0], point2[0]],  # Coordenadas X
        [point1[1], point2[1]],  # Coordenadas Y
        [point1[2], point2[2]],  # Coordenadas Z
        color='red')  # Cor da linha

ax.plot([point1[0] + 2, point2[0]],  # Coordenadas X
        [point1[1], point2[1] + 2],  # Coordenadas Y
        [point1[2], point2[2]],  # Coordenadas Z
        color='red')  # Cor da linha

ax.plot([point1[0] + 2, point2[0]],  # Coordenadas X
        [point1[1] + 2.1, point2[1] + 2.1],  # Coordenadas Y
        [point1[2] + 0.1, point2[2] + 1],  # Coordenadas Z
        color='red')  # Cor da linha

ax.text((point2[0]/2), (point2[1]/2), (point2[2] - 0.3), str(f"{prism1['axes']['x']}m"), color='black', fontsize=16, ha='center', va='center',  bbox=dict(facecolor='red', alpha=0.5))
ax.text((point2[0]), ((point2[1] + 2)/2), (point2[2] - 0.3), str(f"{prism1['axes']['y']}m"), color='black', fontsize=16, ha='center', va='center',  bbox=dict(facecolor='red', alpha=0.5))
ax.text((point2[0] + 0.3), ((point2[1] + 2.3)), ((point2[2] + 1.1)/2), str(f"{prism1['axes']['z']}m"), color='black', fontsize=16, ha='center', va='center',  bbox=dict(facecolor='red', alpha=0.5))

# Set the limits of the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 3])

# Show the plot
plt.show()
