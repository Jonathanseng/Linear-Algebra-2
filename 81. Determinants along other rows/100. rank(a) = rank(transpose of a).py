import numpy as np

def rank(matrix):
  """
  Calculates the rank of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    The rank of the matrix.
  """

  if np.linalg.matrix_rank(matrix) == 0:
    return 0
  else:
    return np.linalg.matrix_rank(transpose(matrix))

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  rank_a = rank(matrix)
  rank_transpose_a = rank(transpose(matrix))
  print(rank_a)
  print(rank_transpose_a)
