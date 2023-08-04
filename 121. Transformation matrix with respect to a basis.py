import numpy as np

def transformation_matrix(basis_vectors, transformation):
  """
  Returns the transformation matrix for the given basis vectors and transformation.

  Args:
    basis_vectors: A list of NumPy arrays representing the basis vectors.
    transformation: A function that takes a vector as input and returns a transformed vector.

  Returns:
    The transformation matrix.
  """

  transformation_matrix = np.zeros((len(basis_vectors), len(basis_vectors)))
  for i, basis_vector in enumerate(basis_vectors):
    transformed_vector = transformation(basis_vector)
    transformation_matrix[i] = transformed_vector

  return transformation_matrix

def main():
  # Define the basis vectors.
  basis_vectors = np.array([[1, 0], [0, 1]])

  # Define the transformation.
  def transformation(vector):
    return 2 * vector

  # Calculate the transformation matrix.
  transformation_matrix = transformation_matrix(basis_vectors, transformation)

  # Print the transformation matrix.
  print(transformation_matrix)

if __name__ == "__main__":
  main()
