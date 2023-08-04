import numpy as np

def eigenvalues_and_eigenvectors(A):
  """
  Calculates the eigenvalues and eigenvectors of A.
  """
  eigenvalues, eigenvectors = np.linalg.eig(A)
  return eigenvalues, eigenvectors

def eigenvectors_and_eigenspaces_for_a_3x3_matrix():
  """
  Example of finding eigenvectors and eigenspaces for a 3x3 matrix.
  """
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(A)
  print("Eigenvalues:")
  print(eigenvalues)
  print("Eigenvectors:")
  print(eigenvectors)
  for i in range(len(eigenvalues)):
    print("Eigenspace for eigenvalue {}:".format(eigenvalues[i]))
    print(eigenvectors[:, i])

if __name__ == '__main__':
  eigenvectors_and_eigenspaces_for_a_3x3_matrix()
