import numpy as np

def vector_combination(A, b):
  """
  Solves a vector combination problem Ax = b.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.

  Returns:
    The solution vector x.
  """

  x = np.linalg.lstsq(A, b)[0]
  return x

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6])
  x = vector_combination(A, b)
  print(x)
