import numpy as np

def least_squares_approximation(x, y):
  """
  Performs least squares approximation of y by a linear function of x.

  Args:
    x: Input data.
    y: Output data.

  Returns:
    Coefficients of the linear function.
  """

  n = len(x)
  A = np.zeros((n, 2))
  for i in range(n):
    A[i, 0] = x[i]
    A[i, 1] = 1
  b = y
  w = np.linalg.lstsq(A, b)[0]
  return w

def main():
  x = np.array([1, 2, 3, 4, 5])
  y = np.array([2, 4, 6, 8, 10])
  w = least_squares_approximation(x, y)
  print(w)

if __name__ == "__main__":
  main()
