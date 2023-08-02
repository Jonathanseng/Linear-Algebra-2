def matrix_addition(A, B):
  """
  Returns the sum of two matrices.

  Args:
    A: The first matrix.
    B: The second matrix.

  Returns:
    The sum of A and B.
  """

  if not A.shape == B.shape:
    raise ValueError("Matrices must have the same shape.")

  result = []
  for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
      row.append(A[i][j] + B[i][j])
    result.append(row)

  return result


def scalar_multiplication(c, A):
  """
  Returns the scalar multiple of a matrix.

  Args:
    c: The scalar.
    A: The matrix.

  Returns:
    The scalar multiple of A.
  """

  result = []
  for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
      row.append(c * A[i][j])
    result.append(row)

  return result


if __name__ == "__main__":
  A = [[1, 2, 3], [4, 5, 6]]
  B = [[7, 8, 9], [10, 11, 12]]
  print(matrix_addition(A, B))
  print(scalar_multiplication(2, A))
