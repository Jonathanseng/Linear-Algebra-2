import numpy as np

def eigenvalues_and_eigenvectors(A):
  """
  Calculates the eigenvalues and eigenvectors of A.
  """
  eigenvalues, eigenvectors = np.linalg.eig(A)
  return eigenvalues, eigenvectors

def eigenvalues_of_a_3x3_matrix():
  """
  Example of finding eigenvalues of a 3x3 matrix.
  """
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(A)
  print("Eigenvalues:")
  print(eigenvalues)

if __name__ == '__main__':
  eigenvalues_of_a_3x3_matrix()
