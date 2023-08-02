def matrix_vector_product(matrix, vector):
  """Applies a matrix to a vector."""
  new_vector = []
  for i in range(len(matrix)):
    dot_product = 0
    for j in range(len(vector)):
      dot_product += matrix[i][j] * vector[j]
    new_vector.append(dot_product)
  return new_vector

def image_of_subset(subset, transformation_matrix):
  """Computes the image of a subset under a transformation."""
  image = []
  for vector in subset:
    image.append(matrix_vector_product(transformation_matrix, vector))
  return image

def main():
  subset = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  transformation_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  image = image_of_subset(subset, transformation_matrix)
  print(image)

if __name__ == "__main__":
  main()
