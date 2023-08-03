import numpy as np

def least_squares_approximation(x, y):
  """
  Performs least squares approximation of the data points (x, y).

  Args:
    x: The x-coordinates of the data points.
    y: The y-coordinates of the data points.

  Returns:
    The coefficients of the least squares approximation.
  """

  n = len(x)
  A = np.zeros((n, 2))
  A[:, 0] = x
  A[:, 1] = 1

  b = np.array(y)

  # Calculate the least squares coefficients.

  coefficients = np.linalg.lstsq(A, b, rcond=-1)[0]

  return coefficients

def main():
  # Create the x-coordinates of the data points.
  x = np.linspace(0, 1, 10)

  # Create the y-coordinates of the data points.
  y = x * x + 2 * x + 1

  # Perform least squares approximation.
  coefficients = least_squares_approximation(x, y)

  # Print the coefficients.
  print(coefficients)

if __name__ == "__main__":
  main()
