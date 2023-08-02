import numpy as np

def complex_eigenvalues_eigenvectors(A):
  """Computes the eigenvalues and eigenvectors of a complex matrix A.

  Args:
    A: The complex matrix.

  Returns:
    A tuple of the eigenvalues and eigenvectors of A.
  """

  # Diagonalize A.
  D, V = np.linalg.eig(A)

  # Check if the eigenvalues are real.
  is_real = np.all(np.imag(D) == 0)

  # If the eigenvalues are real, then the eigenvectors are also real.
  if is_real:
    return D, V

  # If the eigenvalues are complex, then the eigenvectors are also complex.
  else:
    return D, np.dot(V, np.diag(1 / np.imag(V)))

if __name__ == "__main__":
  # Create a complex matrix.
  A = np.array([[1 + 2j, 3 - 4j], [5 + 6j, 7 - 8j]])

  # Compute the eigenvalues and eigenvectors of A.
  D, V = complex_eigenvalues_eigenvectors(A)

  # Print the eigenvalues and eigenvectors of A.
  print("Eigenvalues:", D)
  print("Eigenvectors:", V)
