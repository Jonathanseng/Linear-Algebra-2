def transpose(matrix):
  """
  Calculates the transpose of a matrix.

  Args:
    matrix: A 2D list of numbers.

  Returns:
    The transpose of the matrix.
  """

  transposed_matrix = []
  for i in range(len(matrix[0])):
    transposed_row = []
    for j in range(len(matrix)):
      transposed_row.append(matrix[j][i])
    transposed_matrix.append(transposed_row)
  return transposed_matrix

def product(matrix1, matrix2):
  """
  Calculates the product of two matrices.

  Args:
    matrix1: The first matrix.
    matrix2: The second matrix.

  Returns:
    The product of the two matrices.
  """

  product_matrix = []
  for i in range(len(matrix1)):
    product_row = []
    for j in range(len(matrix2[0])):
      product_element = 0
      for k in range(len(matrix2)):
        product_element += matrix1[i][k] * matrix2[k][j]
      product_row.append(product_element)
    product_matrix.append(product_row)
  return product_matrix

def transpose_product(matrix1, matrix2):
  """
  Calculates the transpose of the product of two matrices.

  Args:
    matrix1: The first matrix.
    matrix2: The second matrix.

  Returns:
    The transpose of the product of the two matrices.
  """

  product_matrix = product(matrix1, matrix2)
  transposed_product_matrix = transpose(product_matrix)
  return transposed_product_matrix

if __name__ == "__main__":
  matrix1 = [[1, 2], [3, 4]]
  matrix2 = [[5, 6], [7, 8]]
  transposed_product = transpose_product(matrix1, matrix2)
  print(transposed_product)
