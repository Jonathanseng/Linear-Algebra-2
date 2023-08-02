def formula_for_2x2_inverse(A):
  """Returns the inverse of a 2x2 matrix A.

  Args:
    A: The 2x2 matrix A.

  Returns:
    The inverse of A.
  """

  # Calculate the determinant of A.
  determinant_of_A = A[0][0] * A[1][1] - A[0][1] * A[1][0]

  # Calculate the inverse of A.
  inverse_of_A = np.array([[A[1][1] / determinant_of_A, -A[0][1] / determinant_of_A],
                              [-A[1][0] / determinant_of_A, A[0][0] / determinant_of_A]])

  return inverse_of_A

if __name__ == "__main__":
  # Create a 2x2 matrix A.
  A = np.array([[1, 2], [3, 4]])

  # Calculate the inverse of A.
  inverse_of_A = formula_for_2x2_inverse(A)

  # Print the inverse of A.
  print(inverse_of_A)
