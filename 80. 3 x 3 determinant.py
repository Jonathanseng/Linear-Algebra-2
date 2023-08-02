def determinant_of_3x3_matrix(A):
  """Returns the determinant of a 3x3 matrix A.

  Args:
    A: The 3x3 matrix A.

  Returns:
    The determinant of A.
  """

  # Calculate the determinant of A.
  determinant_of_A = A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (
      A[1][0] * A[2][2] - A[1][2] * A[2][0]) + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])

  return determinant_of_A

if __name__ == "__main__":
  # Create a 3x3 matrix A.
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  # Calculate the determinant of A.
  determinant_of_A = determinant_of_3x3_matrix(A)

  # Print the determinant of A.
  print(determinant_of_A)
