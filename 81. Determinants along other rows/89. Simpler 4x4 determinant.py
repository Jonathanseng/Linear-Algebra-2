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

def determinant_simple_4x4(matrix):
  """
  Calculates the determinant of a 4x4 matrix using a simpler method.

  Args:
    matrix: A 2D list of numbers.

  Returns:
    The determinant of the matrix.
  """

  cofactors = []
  for i in range(4):
    sub_matrix = matrix[:]
    sub_matrix.pop(i)
    cofactors.append([sub_matrix[j][i] * determinant(sub_matrix[j + 1:]) for j in range(3)])
  return sum([cofactors[i][i] for i in range(4)])

if __name__ == "__main__":
  matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
  print(determinant(matrix))
  print(determinant_simple_4x4(matrix))
