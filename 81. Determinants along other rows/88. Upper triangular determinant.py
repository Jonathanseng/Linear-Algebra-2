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
      sum += matrix[i][0] * determinant(matrix[i + 1:])
    return sum

def determinant_upper_triangular(matrix):
  """
  Calculates the determinant of an upper triangular matrix.

  Args:
    matrix: A 2D list of numbers.

  Returns:
    The determinant of the matrix.
  """

  if len(matrix) == 1:
    return matrix[0][0]
  else:
    return matrix[0][0] * determinant(matrix[1:])

if __name__ == "__main__":
  matrix = [[1, 2, 3], [0, 4, 5], [0, 0, 6]]
  print(determinant(matrix))
  print(determinant_upper_triangular(matrix))
