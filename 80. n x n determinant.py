import numpy as np

def determinant_of_nxn_matrix(A):
  """Returns the determinant of a nxn matrix A.

  Args:
    A: The nxn matrix A.

  Returns:
    The determinant of A.
  """

  # Check if the matrix is square.
  if A.shape[0] != A.shape[1]:
    raise ValueError("The matrix A is not square.")

  # Calculate the determinant of A recursively.
  if A.shape[0] == 1:
    return A[0][0]
  else:
    return sum([A[0][i] * determinant_of_nxn_matrix(A[1:, :].copy()) for i in range(A.shape[0])])

if __name__ == "__main__":
  # Create an nxn matrix A.
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  # Calculate the determinant of A.
  determinant_of_A = determinant_of_nxn_matrix(A)

  # Print the determinant of A.
  print(determinant_of_A)
