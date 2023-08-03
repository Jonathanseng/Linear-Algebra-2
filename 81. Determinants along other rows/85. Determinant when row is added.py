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

def determinant_row_add(matrix, row1, row2):
  """
  Calculates the determinant of a matrix when a row is added to another row.

  Args:
    matrix: A 2D list of numbers.
    row1: The row to add to the other row.
    row2: The row to add to row1.

  Returns:
    The determinant of the matrix.
  """

  new_matrix = matrix[:]
  new_matrix[row2] = [x + y for x, y in zip(new_matrix[row1], new_matrix[row2])]
  return determinant(new_matrix)

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print(determinant(matrix))
  print(determinant_row_add(matrix, 0, 1))
