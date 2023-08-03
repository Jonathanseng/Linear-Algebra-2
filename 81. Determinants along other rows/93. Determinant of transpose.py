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

def determinant_transpose(matrix):
  """
  Calculates the determinant of a matrix's transpose.

  Args:
    matrix: A 2D list of numbers.

  Returns:
    The determinant of the transpose of the matrix.
  """

  transposed_matrix = transpose(matrix)
  return determinant(transposed_matrix)

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  determinant_transpose = determinant_transpose(matrix)
  print(determinant_transpose)
