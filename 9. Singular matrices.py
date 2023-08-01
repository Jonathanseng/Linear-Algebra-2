import numpy as np

def is_singular(A):
  """
  Checks if a matrix is singular.

  Args:
    A: The matrix to check.

  Returns:
    True if the matrix is singular, False otherwise.
  """

  return np.linalg.det(A) == 0

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  print(is_singular(A))

  A = np.array([[1, 0], [0, 0]])
  print(is_singular(A))
