import matplotlib.pyplot as plt
import numpy as np

def rowspace(matrix):
  """
  Calculates the rowspace of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    The rowspace of the matrix.
  """

  rowspace = []
  for i in range(len(matrix)):
    row = matrix[i]
    rowspace.append(row)
  return rowspace

def left_nullspace(matrix):
  """
  Calculates the left nullspace of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    The left nullspace of the matrix.
  """

  left_nullspace = []
  for i in range(len(matrix)):
    row = [0 for _ in range(len(matrix[0]))]
    row[i] = 1
    left_nullspace.append(row)
  return left_nullspace

def visualize_rowspace(matrix):
  """
  Visualizes the rowspace of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    None.
  """

  rowspace = rowspace(matrix)
  for row in rowspace:
    plt.plot(row)
  plt.show()

def visualize_left_nullspace(matrix):
  """
  Visualizes the left nullspace of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    None.
  """

  left_nullspace = left_nullspace(matrix)
  for row in left_nullspace:
    plt.plot(row)
  plt.show()

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  visualize_rowspace(matrix)
  visualize_left_nullspace(matrix)
