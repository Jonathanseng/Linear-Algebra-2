import numpy as np

def parametric_line(x0, y0, x1, y1, t):
  """
  Returns the parametric representation of a line.

  Args:
    x0: The x-coordinate of the first point on the line.
    y0: The y-coordinate of the first point on the line.
    x1: The x-coordinate of the second point on the line.
    y1: The y-coordinate of the second point on the line.
    t: The parameter.

  Returns:
    The parametric representation of the line.
  """

  x = x0 + t * (x1 - x0)
  y = y0 + t * (y1 - y0)

  return np.array([x, y])

def main():
  """
  The main function.
  """

  x0 = 1
  y0 = 2
  x1 = 3
  y1 = 4

  t = 0.5

  line = parametric_line(x0, y0, x1, y1, t)

  print(line)

if __name__ == "__main__":
  main()
