import numpy as np

def change_of_basis(basis_vectors):
  """
  Returns the invertible change of basis matrix for the given basis vectors.

  Args:
    basis_vectors: A list of NumPy arrays representing the basis vectors.

  Returns:
    The invertible change of basis matrix.
  """

  change_of_basis_matrix = np.transpose(basis_vectors)
  if np.linalg.det(change_of_basis_matrix) == 0:
    raise ValueError("The given basis vectors do not form an invertible basis.")

  return np.linalg.inv(change_of_basis_matrix)

def main():
  # Define the basis vectors.
  basis_vectors = np.array([[1, 0], [0, 1]])

  # Calculate the change of basis matrix.
  change_of_basis_matrix = change_of_basis(basis_vectors)

  # Print the change of basis matrix.
  print(change_of_basis_matrix)

if __name__ == "__main__":
  main()
