import numpy as np

def eigenvalues_and_eigenvectors(A):
  """
  Calculates the eigenvalues and eigenvectors of A.
  """
  eigenvalues, eigenvectors = np.linalg.eig(A)
  return eigenvalues, eigenvectors

def finding_eigenvectors_and_eigenspaces_example():
  """
  Example of finding eigenvectors and eigenspaces.
  """
  A = np.array([[2, 1], [1, 2]])
  eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(A)
  print("Eigenvalues:")
  print(eigenvalues)
  print("Eigenvectors:")
  print(eigenvectors)
  for i in range(len(eigenvalues)):
    print("Eigenspace for eigenvalue {}:".format(eigenvalues[i]))
    print(eigenvectors[:, i])

if __name__ == '__main__':
  finding_eigenvectors_and_eigenspaces_example()
