def matrix_vector_product(matrix, vector):
  """Computes the matrix-vector product of two matrices."""
  product = []
  for i in range(len(matrix)):
    row_product = 0
    for j in range(len(vector)):
      row_product += matrix[i][j] * vector[j]
    product.append(row_product)
  return product

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  vector = [1, 2, 3]
  product = matrix_vector_product(matrix, vector)
  print("The matrix-vector product is:", product)
