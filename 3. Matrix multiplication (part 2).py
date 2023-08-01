import numpy as np

def matrix_multiplication_optimized(A, B):
  """
  Performs matrix multiplication of the matrices A and B in a more optimized way.

  Args:
    A: The first matrix.
    B: The second matrix.

  Returns:
    C: The product of the matrices A and B.
  """

  n = A.shape[0]
  m = A.shape[1]
  p = B.shape[1]
  C = np.zeros((n, p))

  for i in range(n):
    row_i = A[i, :]
    for j in range(p):
      column_j = B[:, j]
      C[i, j] = np.dot(row_i, column_j)

  return C

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  B = np.array([[5, 6], [7, 8]])
  C = matrix_multiplication_optimized(A, B)
  print(C)
