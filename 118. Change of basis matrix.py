import numpy as np

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
  return change_of_basis_matrix

def main():
  old_basis = np.array([[1, 0], [0, 1]])
  new_basis = np.array([[1, 1], [1, -1]])
  change_of_basis_matrix = change_of_basis_matrix(old_basis, new_basis)
  print(change_of_basis_matrix)

if __name__ == "__main__":
  main()
