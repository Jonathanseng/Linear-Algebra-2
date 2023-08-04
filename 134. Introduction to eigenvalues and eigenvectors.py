import numpy as np

def eigenvalues_and_eigenvectors(A):
  """
  Calculates the eigenvalues and eigenvectors of A.
  """
  eigenvalues, eigenvectors = np.linalg.eig(A)
  return eigenvalues, eigenvectors

if __name__ == '__main__':
  A = np.array([[2, 1], [1, 2]])
  eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(A)
  print(eigenvalues)
  print(eigenvectors)
