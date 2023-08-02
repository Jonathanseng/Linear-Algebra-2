import numpy as np
import matplotlib.pyplot as plt

def visualize_diagonalization(A, D, V):
  """Visualizes the diagonalization of a matrix A.

  Args:
    A: The matrix to be diagonalized.
    D: The diagonal matrix of A.
    V: The eigenvectors of A.
  """

  # Plot the eigenvalues of A.
  plt.plot(D, 'o')
  plt.xlabel("Eigenvalue index")
  plt.ylabel("Eigenvalue")

  # Plot the eigenvectors of A.
  for i in range(len(D)):
    v = V[:, i]
    plt.plot([0, 1], v, '--')
  plt.xlabel("Coordinate")
  plt.ylabel("Eigenvector")

if __name__ == "__main__":
  # Create a matrix.
  A = np.array([[1, 2], [3, 4]])

  # Diagonalize A.
  D, V = np.linalg.eig(A)

  # Visualize the diagonalization of A.
  visualize_diagonalization(A, D, V)

  # Show the plot.
  plt.show()
