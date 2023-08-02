def rref(matrix):
  """Computes the reduced row echelon form of a matrix."""
  n = len(matrix)
  for i in range(n):
    # Find the pivot element in column i.
    pivot_row = i
    for j in range(i + 1, n):
      if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
        pivot_row = j

    # Swap rows i and pivot_row.
    if pivot_row != i:
      matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

    # Make all other entries in column i equal to 0.
    for j in range(n):
      if j != i:
        factor = matrix[j][i] / matrix[i][i]
        for k in range(n):
          matrix[j][k] -= factor * matrix[i][k]

    # Make all leading entries equal to 1.
    if matrix[i][i] != 0:
      for j in range(n):
        matrix[i][j] /= matrix[i][i]

  return matrix

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  rref_matrix = rref(matrix)
  print("The reduced row echelon form of the matrix is:", rref_matrix)
