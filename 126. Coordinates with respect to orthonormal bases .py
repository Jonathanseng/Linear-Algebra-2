import numpy as np

def coordinates_with_respect_to_orthonormal_basis(vector, basis):
  """
  Returns the coordinates of the given vector with respect to the given orthonormal basis.

  Args:
    vector: A NumPy array representing the vector.
    basis: A list of NumPy arrays representing the orthonormal basis.

  Returns:
    The coordinates of the vector.
  """

  coordinates = np.zeros(len(basis))
  for i, basis_vector in enumerate(basis):
    coordinates[i] = np.dot(vector, basis_vector)

  return coordinates

def main():
  # Define the vector.
  vector = np.array([1, 0])

  # Define the orthonormal basis.
  basis = np.array([[1, 0], [0, 1]])

  # Calculate the coordinates of the vector.
  coordinates = coordinates_with_respect_to_orthonormal_basis(vector, basis)

  # Print the coordinates of the vector.
  print(coordinates)

if __name__ == "__main__":
  main()
