import numpy as np

def eigenvalues_and_eigenvectors(A):
  """
  Calculates the eigenvalues and eigenvectors of A.
  """
  eigenvalues, eigenvectors = np.linalg.eig(A)
  return eigenvalues, eigenvectors

def example_solving_for_eigenvalues_of_a_2x2_matrix():
  """
  Example of solving for the eigenvalues of a 2x2 matrix.
  """
  A = np.array([[2, 1], [1, 2]])
  eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(A)
  print(eigenvalues)
  print(eigenvectors)

if __name__ == '__main__':
  example_solving_for_eigenvalues_of_a_2x2_matrix()
