def null_space(matrix):
  """Computes the null space of a matrix."""
  n = len(matrix)
  null_space = []
  for i in range(n):
    vector = [0 for _ in range(n)]
    vector[i] = 1
    if matrix_vector_product(matrix, vector) == [0 for _ in range(n)]:
      null_space.append(vector)
  return null_space

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  null_space_vectors = null_space(matrix)
  print("The null space of the matrix is:", null_space_vectors)
