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

def determinant_along_row(matrix, row):
  """
  Calculates the determinant of a matrix along a given row.

  Args:
    matrix: A 2D list of numbers.
    row: The row to calculate the determinant along.

  Returns:
    The determinant of the matrix along the given row.
  """

  sub_matrix = matrix[:]
  sub_matrix.pop(row)
  return determinant(sub_matrix)

def determinant_along_col(matrix, col):
  """
  Calculates the determinant of a matrix along a given column.

  Args:
    matrix: A 2D list of numbers.
    col: The column to calculate the determinant along.

  Returns:
    The determinant of the matrix along the given column.
  """

  sub_matrix = []
  for i in range(len(matrix)):
    sub_matrix.append(matrix[i][:])
    sub_matrix[i].pop(col)
  return determinant(sub_matrix)

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print(determinant(matrix))
  print(determinant_along_row(matrix, 0))
  print(determinant_along_col(matrix, 0))
