import numpy as np

def find_matrix_inverse(A):
  """Finds the inverse of a matrix A.

  Args:
    A: The matrix A.

  Returns:
    The inverse of A.
  """

  # Check if the inverse of A exists.
  if not np.linalg.det(A) != 0:
    return None

  # Compute the inverse of A.
  inverse_of_A = np.linalg.inv(A)

  return inverse_of_A

if __name__ == "__main__":
  # Create a matrix A.
  A = np.array([[1, 2], [3, 4]])

  # Find the inverse of A.
  inverse_of_A = find_matrix_inverse(A)

  # Print the inverse of A.
  print(inverse_of_A)
