import numpy as np

def eigenvalues_and_eigenvectors(A):
  """
  Calculates the eigenvalues and eigenvectors of A.
  """
  eigenvalues, eigenvectors = np.linalg.eig(A)
  return eigenvalues, eigenvectors

def showing_that_an_eigenbasis_makes_for_good_coordinate_systems():
  """
  Example of showing that an eigenbasis makes for good coordinate systems.
  """
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(A)
  print("Eigenvalues:")
  print(eigenvalues)
  print("Eigenvectors:")
  print(eigenvectors)
  print("Projection of a vector onto the eigenspace for eigenvalue 5:")
  v = np.array([1, 2, 3])
  projection = np.dot(v, eigenvectors[:, 0]) * eigenvectors[:, 0]
  print(projection)

if __name__ == '__main__':
  showing_that_an_eigenbasis_makes_for_good_coordinate_systems()
