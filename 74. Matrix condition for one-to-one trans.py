import numpy as np

def matrix_condition_for_one_to_one_transformation(A):
  """Checks if a matrix A represents a one-to-one transformation.

  Args:
    A: The matrix A.

  Returns:
    True if A represents a one-to-one transformation, False otherwise.
  """

  # Check if the determinant of A is nonzero.
  if np.linalg.det(A) != 0:
    # The determinant of A is nonzero, so A represents a one-to-one transformation.
    return True
  else:
    # The determinant of A is zero, so A does not represent a one-to-one transformation.
    return False

if __name__ == "__main__":
  # Create a matrix A.
  A = np.array([[1, 2], [3, 4]])

  # Check if A represents a one-to-one transformation.
  if matrix_condition_for_one_to_one_transformation(A):
    print("The matrix A represents a one-to-one transformation.")
  else:
    print("The matrix A does not represent a one-to-one transformation.")
