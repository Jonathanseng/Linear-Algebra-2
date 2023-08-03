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

def area_of_parallelogram(matrix):
  """
  Calculates the area of a parallelogram from the determinant of its matrix.

  Args:
    matrix: A 2D list of numbers.

  Returns:
    The area of the parallelogram.
  """

  return abs(determinant(matrix))

if __name__ == "__main__":
  matrix = [[1, 2], [3, 4]]
  print(area_of_parallelogram(matrix))
