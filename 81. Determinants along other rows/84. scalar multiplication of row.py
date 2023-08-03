def scalar_multiplication_of_row(matrix, row, scalar):
  """
  Multiplies a row of a matrix by a scalar.

  Args:
    matrix: A 2D list of numbers.
    row: The row to multiply by the scalar.
    scalar: The scalar to multiply the row by.

  Returns:
    A new matrix with the specified row multiplied by the scalar.
  """

  new_matrix = matrix[:]
  new_matrix[row] = [scalar * x for x in new_matrix[row]]
  return new_matrix

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  new_matrix = scalar_multiplication_of_row(matrix, 0, 2)
  print(new_matrix)
