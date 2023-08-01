import numpy as np

def invert_matrix(A):
  """
  Inverts the 2x2 matrix A.

  Args:
    A: The 2x2 matrix to be inverted.

  Returns:
    B: The inverse of the matrix A.
  """

  det = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
  B = np.zeros_like(A)
  B[0, 0] = A[1, 1] / det
  B[0, 1] = -A[0, 1] / det
  B[1, 0] = -A[1, 0] / det
  B[1, 1] = A[0, 0] / det

  return B

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  B = invert_matrix(A)
  print(B)
