def column_space(matrix):
  """Computes the column space of a matrix."""
  column_space = []
  for i in range(len(matrix)):
    column = matrix[:, i]
    column_space.append(column)
  return column_space

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  column_space_vectors = column_space(matrix)
  print("The column space of the matrix is:", column_space_vectors)
