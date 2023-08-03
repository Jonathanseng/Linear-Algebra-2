def determinant(matrix):
  """
  Calculates the determinant of a matrix.

  Args:
    matrix: A 2D list of numbers.

  Returns:
    The determinant of the matrix.
  """

  if len(matrix) == 1:
    return matrix[0][0]
  else:
    sum = 0
    for i in range(len(matrix)):
      sub_matrix = matrix[:]
      sub_matrix.pop(i)
      sum += matrix[i][0] * determinant(sub_matrix) * (-1 if i % 2 else 1)
    return sum

def determinant_row_scalar(matrix, row, scalar):
  """
  Calculates the determinant of a matrix when a row is multiplied by a scalar.

  Args:
    matrix: A 2D list of numbers.
    row: The row to multiply by the scalar.
    scalar: The scalar to multiply the row by.

  Returns:
    The determinant of the matrix.
  """

  sub_matrix = matrix[:]
  sub_matrix[row] = [scalar * x for x in sub_matrix[row]]
  return determinant(sub_matrix)

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print(determinant(matrix))
  print(determinant_row_scalar(matrix, 0, 2))
