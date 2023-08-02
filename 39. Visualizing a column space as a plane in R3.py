import matplotlib.pyplot as plt
import numpy as np

def visualize_column_space(matrix):
  """Visualizes the column space of a matrix as a plane in R3."""
  column_space = column_space(matrix)
  x_coords = []
  y_coords = []
  z_coords = []
  for vector in column_space:
    x_coords.append(vector[0])
    y_coords.append(vector[1])
    z_coords.append(vector[2])
  plt.plot(x_coords, y_coords, z_coords, 'b-')
  plt.show()

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  visualize_column_space(matrix)
