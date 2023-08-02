def matrix_vector_product(matrix, vector):
  """Applies a matrix to a vector."""
  new_vector = []
  for i in range(len(matrix)):
    dot_product = 0
    for j in range(len(vector)):
      dot_product += matrix[i][j] * vector[j]
    new_vector.append(dot_product)
  return new_vector

def linear_transformation(vector, transformation_matrix):
  """Applies a linear transformation matrix to a vector."""
  new_vector = matrix_vector_product(transformation_matrix, vector)
  return new_vector

def main():
  vector = [1, 2, 3]
  transformation_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  new_vector = linear_transformation(vector, transformation_matrix)
  print(new_vector)

if __name__ == "__main__":
  main()
