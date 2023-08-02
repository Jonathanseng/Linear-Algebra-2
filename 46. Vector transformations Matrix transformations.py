def vector_transformation(vector, transformation_matrix):
  """Applies a transformation matrix to a vector."""
  new_vector = []
  for i in range(len(vector)):
    dot_product = 0
    for j in range(len(vector)):
      dot_product += vector[j] * transformation_matrix[i][j]
    new_vector.append(dot_product)
  return new_vector

def matrix_transformation(matrix, transformation_matrix):
  """Applies a transformation matrix to a matrix."""
  new_matrix = []
  for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[0])):
      dot_product = 0
      for k in range(len(matrix[0])):
        dot_product += matrix[i][k] * transformation_matrix[k][j]
      new_row.append(dot_product)
    new_matrix.append(new_row)
  return new_matrix

def main():
  vector = [1, 2, 3]
  transformation_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  new_vector = vector_transformation(vector, transformation_matrix)
  print(new_vector)

  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  new_matrix = matrix_transformation(matrix, transformation_matrix)
  print(new_matrix)

if __name__ == "__main__":
  main()
