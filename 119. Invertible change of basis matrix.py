import numpy as np

def is_invertible(matrix):
  """
  Checks if matrix is invertible.

  Args:
    matrix: Matrix to check.

  Returns:
    True if matrix is invertible, False otherwise.
  """

  determinant = np.linalg.det(matrix)
  return determinant != 0

def change_of_basis_matrix(old_basis, new_basis):
  """
  Calculates the change of basis matrix from old_basis to new_basis.

  Args:
    old_basis: Old basis.
    new_basis: New basis.

  Returns:
    Change of basis matrix.
  """

  change_of_basis_matrix = np.zeros((len(new_basis), len(old_basis)))
  for i in range(len(new_basis)):
    for j in range(len(old_basis)):
      change_of_basis_matrix[i, j] = np.dot(new_basis[i], old_basis[j])

  if not is_invertible(change_of_basis_matrix):
    raise ValueError("Change of basis matrix is not invertible")

  return change_of_basis_matrix

def main():
  old_basis = np.array([[1, 0], [0, 1]])
  new_basis = np.array([[1, 1], [1, -1]])
  change_of_basis_matrix = change_of_basis_matrix(old_basis, new_basis)
  print(change_of_basis_matrix)

if __name__ == "__main__":
  main()
