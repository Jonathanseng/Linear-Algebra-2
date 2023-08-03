def transpose(matrix):
  """
  Calculates the transpose of a matrix.

  Args:
    matrix: A 2D list of numbers.

  Returns:
    The transpose of the matrix.
  """

  transposed_matrix = []
  for i in range(len(matrix[0])):
    transposed_row = []
    for j in range(len(matrix)):
      transposed_row.append(matrix[j][i])
    transposed_matrix.append(transposed_row)
  return transposed_matrix

def sum_transpose(matrix1, matrix2):
  """
  Calculates the transpose of the sum of two matrices.

  Args:
    matrix1: The first matrix.
    matrix2: The second matrix.

  Returns:
    The transpose of the sum of the two matrices.
  """

  transposed_matrix1 = transpose(matrix1)
  transposed_matrix2 = transpose(matrix2)
  sum_transpose_matrix = transposed_matrix1 + transposed_matrix2
  return sum_transpose_matrix

def inverse_transpose(matrix):
  """
  Calculates the transpose of the inverse of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    The transpose of the inverse of the matrix.
  """

  inverse_matrix = inverse(matrix)
  transposed_inverse_matrix = transpose(inverse_matrix)
  return transposed_inverse_matrix

def inverse(matrix):
  """
  Calculates the inverse of a matrix.

  Args:
    matrix: The matrix.

  Returns:
    The inverse of the matrix.
  """

  determinant = determinant(matrix)
  if determinant == 0:
    return None
  else:
    return [[matrix[j][i] / determinant for i in range(len(matrix))] for j in range(len(matrix))]

if __name__ == "__main__":
  matrix1 = [[1, 2], [3, 4]]
  matrix2 = [[5, 6], [7, 8]]
  sum_transpose = sum_transpose(matrix1, matrix2)
  print(sum_transpose)
  inverse_transpose = inverse_transpose(matrix1)
  print(inverse_transpose)
