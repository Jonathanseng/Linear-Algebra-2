import numpy as np

def power_of_matrix_via_diagonalization(A, n):
  """Computes the nth power of a matrix A via diagonalization.

  Args:
    A: The matrix to be raised to the nth power.
    n: The exponent.

  Returns:
    The nth power of A.
  """

  # Diagonalize A.
  D, V = np.linalg.eig(A)

  # Compute the nth power of D.
  D_n = np.power(D, n)

  # Compute the nth power of V.
  V_n = np.linalg.matrix_power(V, n)

  # Return the product of D_n and V_n.
  return np.dot(D_n, V_n)

if __name__ == "__main__":
  # Create a matrix.
  A = np.array([[1, 2], [3, 4]])

  # Compute the 5th power of A.
  A_5 = power_of_matrix_via_diagonalization(A, 5)

  # Print the 5th power of A.
  print(A_5)
