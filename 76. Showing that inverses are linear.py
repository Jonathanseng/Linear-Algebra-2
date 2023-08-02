import numpy as np

def show_that_inverses_are_linear(A):
  """Shows that the inverse of a linear transformation is also linear.

  Args:
    A: The matrix A.

  Returns:
    True if the inverse of A is linear, False otherwise.
  """

  # Check if the inverse of A exists.
  if not np.linalg.det(A) != 0:
    return False

  # Create a vector x.
  x = np.array([1, 2])

  # Compute the inverse of A.
  inverse_of_A = np.linalg.inv(A)

  # Check if the inverse of A is linear.
  for scalar in [1, 2, 3]:
    for vector in [x, 2 * x, 3 * x]:
      # Check if the inverse of A is linear.
      if inverse_of_A @ (scalar * vector) != scalar * inverse_of_A @ vector:
        return False

  return True

if __name__ == "__main__":
  # Create a matrix A.
  A = np.array([[1, 2], [3, 4]])

  # Show that the inverse of A is linear.
  if show_that_inverses_are_linear(A):
    print("The inverse of A is linear.")
  else:
    print("The inverse of A is not linear.")
