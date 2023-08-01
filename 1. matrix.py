import numpy as np

def create_matrix(n, m):
  """
  Creates a matrix of size n x m.

  Args:
    n: The number of rows in the matrix.
    m: The number of columns in the matrix.

  Returns:
    A: The matrix.
  """

  A = np.zeros((n, m))

  return A

def print_matrix(A):
  """
  Prints the matrix A.

  Args:
    A: The matrix to be printed.
  """

  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      print(A[i, j], end=' ')
    print()

if __name__ == "__main__":
  A = create_matrix(3, 2)
  print_matrix(A)
