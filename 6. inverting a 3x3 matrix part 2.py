import numpy as np

def determinant(A):
  """
  Calculates the determinant of the 3x3 matrix A.

  Args:
    A: The 3x3 matrix to be inverted.

  Returns:
    det: The determinant of the matrix A.
  """

  det = A[0, 0] * (A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1])
  det -= A[0, 1] * (A[1, 0] * A[2, 2] - A[1, 2] * A[2, 0])
  det += A[0, 2] * (A[1, 0] * A[2, 1] - A[1, 1] * A[2, 0])

  return det

def invert_matrix_part2(A, det):
  """
  Inverts the 3x3 matrix A, part 2.

  Args:
    A: The 3x3 matrix to be inverted.
    det: The determinant of the matrix A.

  Returns:
    B: The inverse of the matrix A.
  """

  B = np.zeros_like(A)
  B[0, 0] = (A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1]) / det
  B[0, 1] = (-A[0, 1] * A[2, 2] + A[0, 2] * A[2, 1]) / det
  B[0, 2] = (A[0, 1] * A[1, 2] - A[0, 2] * A[1, 1]) / det
  B[1, 0] = (-A[1, 0] * A[2, 2] + A[1, 2] * A[2, 0]) / det
  B[1, 1] = (A[0, 0] * A[2, 2] - A[0, 2] * A[2, 0]) / det
  B[1, 2] = (-A[0, 0] * A[1, 2] + A[0, 2] * A[1, 0]) / det
  B[2, 0] = (A[1, 0] * A[2, 1] - A[1, 1] * A[2, 0]) / det
  B[2, 1] = (-A[0, 0] * A[2, 1] + A[0, 1] * A[2, 0]) / det
  B[2, 2] = (A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]) / det

  return B

if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  det = determinant(A)
  B = invert_matrix_part2(A, det)
  print(B)
