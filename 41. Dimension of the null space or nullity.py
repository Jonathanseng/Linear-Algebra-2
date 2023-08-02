def null_space(matrix):
  """Computes the null space of a matrix."""
  rref_matrix = rref(matrix)
  null_space = []
  for i in range(len(rref_matrix)):
    if rref_matrix[i][i] == 0:
      null_space.append([0 for _ in range(len(rref_matrix))])
    else:
      vector = [0 for _ in range(len(rref_matrix))]
      vector[i] = 1
      null_space.append(vector)
  return null_space

def dimension_of_null_space(matrix):
  """Computes the dimension of the null space of a matrix."""
  null_space = null_space(matrix)
  return len(null_space)

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print("The dimension of the null space of the matrix is:",
        dimension_of_null_space(matrix))
