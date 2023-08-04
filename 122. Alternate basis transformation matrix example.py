import numpy as np

def alternate_basis_transformation_matrix(basis_vectors1, basis_vectors2):
  """
  Returns the alternate basis transformation matrix for the given basis vectors.

  Args:
    basis_vectors1: A list of NumPy arrays representing the first basis vectors.
    basis_vectors2: A list of NumPy arrays representing the second basis vectors.

  Returns:
    The alternate basis transformation matrix.
  """

  transformation_matrix = np.zeros((len(basis_vectors2), len(basis_vectors1)))
  for i, basis_vector2 in enumerate(basis_vectors2):
    for j, basis_vector1 in enumerate(basis_vectors1):
      transformation_matrix[i][j] = np.dot(basis_vector2, basis_vector1)

  return transformation_matrix

def main():
  # Define the first basis vectors.
  basis_vectors1 = np.array([[1, 0], [0, 1]])

  # Define the second basis vectors.
  basis_vectors2 = np.array([[1, 1], [1, -1]])

  # Calculate the alternate basis transformation matrix.
  transformation_matrix = alternate_basis_transformation_matrix(basis_vectors1, basis_vectors2)

  # Print the alternate basis transformation matrix.
  print(transformation_matrix)

if __name__ == "__main__":
  main()
