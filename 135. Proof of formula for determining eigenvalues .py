import numpy as np

def eigenvalues_and_eigenvectors(A):
  """
  Calculates the eigenvalues and eigenvectors of A.
  """
  eigenvalues, eigenvectors = np.linalg.eig(A)
  return eigenvalues, eigenvectors

def proof_of_formula(A, v):
  """
  Proof of the formula for determining eigenvalues.
  """
  eigenvalue = np.dot(v, np.dot(A, v)) / np.dot(v, v)
  return eigenvalue

if __name__ == '__main__':
  A = np.array([[2, 1], [1, 2]])
  v = np.array([1, 0])
  eigenvalue = proof_of_formula(A, v)
  print(eigenvalue)
