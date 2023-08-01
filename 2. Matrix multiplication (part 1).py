import numpy as np

def matrix_multiplication(A, B):
  """
  Performs matrix multiplication of the matrices A and B.

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
    for j in range(p):
      for k in range(m):
        C[i, j] += A[i, k] * B[k, j]

  return C

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  B = np.array([[5, 6], [7, 8]])
  C = matrix_multiplication(A, B)
  print(C)
