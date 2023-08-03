def determinant_sarrusch(matrix):
  """
  Calculates the determinant of a matrix using the Rule of Sarrus.

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
      product = 1
      for j in range(len(matrix)):
        if i != j:
          product *= matrix[i][j]
      sum += product
    return sum

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print(determinant_sarrusch(matrix))
