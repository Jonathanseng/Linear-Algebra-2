import numpy as np

def nullspace(matrix):
  """
  Calculates the nullspace of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    The nullspace of the matrix.
  """

  nullspace = []
  for i in range(len(matrix)):
    row = [0 for _ in range(len(matrix[0]))]
    row[i] = 1
    if row in matrix:
      nullspace.append(row)
  return nullspace

def orthogonal_complement(matrix):
  """
  Calculates the orthogonal complement of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    The orthogonal complement of the matrix.
  """

  rowspace = rowspace(matrix)
  left_nullspace = left_nullspace(matrix)
  orthogonal_complement = []
  for i in range(len(matrix[0])):
    row = [0 for _ in range(len(matrix[0]))]
    row[i] = 1
    if row not in rowspace and row not in left_nullspace:
      orthogonal_complement.append(row)
  return orthogonal_complement

def main():
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  nullspace_matrix = nullspace(matrix)
  orthogonal_complement_nullspace = orthogonal_complement(nullspace_matrix)
  print(orthogonal_complement_nullspace)

if __name__ == "__main__":
  main()
