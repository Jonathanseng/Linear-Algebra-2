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

def column_space(matrix):
  """Computes the column space of a matrix."""
  column_space = []
  for i in range(len(matrix)):
    column = matrix[:, i]
    column_space.append(column)
  return column_space

def basis(vectors):
  """Returns a basis for the set of vectors."""
  basis = []
  for vector in vectors:
    if not any(vector == b for b in basis):
      basis.append(vector)
  return basis

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  null_space_vectors = null_space(matrix)
  column_space_vectors = column_space(matrix)
  print("The null space basis is:", basis(null_space_vectors))
  print("The column space basis is:", basis(column_space_vectors))
