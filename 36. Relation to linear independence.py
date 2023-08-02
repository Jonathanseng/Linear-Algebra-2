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

def is_linear_independent(vectors):
  """Checks if a list of vectors is linearly independent."""
  for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
      if dot_product(vectors[i], vectors[j]) != 0:
        return False
  return True

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  null_space_vectors = null_space(matrix)
  print("The null space of the matrix is:", null_space_vectors)
  print("The vectors in the null space are linearly independent:",
        is_linear_independent(null_space_vectors))
