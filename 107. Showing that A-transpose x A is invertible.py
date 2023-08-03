import numpy as np

def is_invertible(A):
  """
  Checks if the matrix A is invertible.

  Args:
    A: The matrix A.

  Returns:
    True if A is invertible, False otherwise.
  """

  n = A.shape[0]

  # Check that the matrix has full rank.

  if np.linalg.matrix_rank(A) != n:
    return False

  # Check that the determinant of A is non-zero.

  determinant = np.linalg.det(A)
  if determinant == 0:
    return False

  # The matrix is invertible.

  return True

def main():
  # Create the matrix A.
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  # Check if A is invertible.
  is_invertible_A = is_invertible(A)

  # Print the result.
  print(is_invertible_A)

if __name__ == "__main__":
  main()
