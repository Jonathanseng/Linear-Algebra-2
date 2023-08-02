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


if __name__ == "__main__":
  A = [[1, 2], [3, 4]]
  B = [[5, 6], [7, 8]]
  print(matrix_product(A, B))
