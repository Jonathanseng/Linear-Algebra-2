def column_space(matrix):
  """Computes the column space of a matrix."""
  column_space = []
  for i in range(len(matrix)):
    column = matrix[:, i]
    column_space.append(column)
  return column_space

def dimension_of_column_space(matrix):
  """Computes the dimension of the column space of a matrix."""
  column_space = column_space(matrix)
  return len(column_space)

def rank(matrix):
  """Computes the rank of a matrix."""
  return dimension_of_column_space(matrix)

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print("The rank of the matrix is:", rank(matrix))
