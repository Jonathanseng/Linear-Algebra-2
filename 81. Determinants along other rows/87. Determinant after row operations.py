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

def determinant_row_operations(matrix, operations):
  """
  Calculates the determinant of a matrix after row operations.

  Args:
    matrix: A 2D list of numbers.
    operations: A list of row operations to perform on the matrix.

  Returns:
    The determinant of the matrix after the row operations are performed.
  """

  for operation in operations:
    if operation == "R1 + R2":
      matrix[0] += matrix[1]
    elif operation == "R1 - R2":
      matrix[0] -= matrix[1]
  return determinant(matrix)

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  operations = ["R1 + R2"]
  print(determinant(matrix))
  print(determinant_row_operations(matrix, operations))
