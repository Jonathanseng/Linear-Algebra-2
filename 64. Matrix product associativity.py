def matrix_product(A, B):
  """
  Returns the product of the matrices A and B.

  Args:
    A: The first matrix.
    B: The second matrix.

  Returns:
    The product of the matrices A and B.
  """

  product = []
  for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
      dot_product = 0
      for k in range(len(A[0])):
        dot_product += A[i][k] * B[k][j]
      row.append(dot_product)
    product.append(row)

  return product


def matrix_associativity(A, B, C):
  """
  Returns True if the matrix product is associative, False otherwise.

  Args:
    A: The first matrix.
    B: The second matrix.
    C: The third matrix.

  Returns:
    True if the matrix product is associative, False otherwise.
  """

  product1 = matrix_product(A, matrix_product(B, C))
  product2 = matrix_product(matrix_product(A, B), C)
  return product1 == product2


if __name__ == "__main__":
  A = [[1, 2], [3, 4]]
  B = [[5, 6], [7, 8]]
  C = [[9, 10], [11, 12]]
  print(matrix_associativity(A, B, C))
