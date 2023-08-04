import numpy as np

def projection_onto_subspace(vector, basis):
  """
  Returns the projection of the given vector onto the given subspace spanned by the orthonormal basis.

  Args:
    vector: A NumPy array representing the vector.
    basis: A list of NumPy arrays representing the orthonormal basis.

  Returns:
    The projection of the vector.
  """

  # Calculate the projection matrix.
  projection_matrix = np.dot(basis, basis.T)

  # Calculate the projection of the vector.
  projection = np.dot(projection_matrix, vector)

  return projection

def main():
  # Define the vector.
  vector = np.array([1, 0])

  # Define the orthonormal basis.
  basis = np.array([[1, 0], [0, 1]])

  # Calculate the projection of the vector.
  projection = projection_onto_subspace(vector, basis)

  # Print the projection of the vector.
  print(projection)

if __name__ == "__main__":
  main()
