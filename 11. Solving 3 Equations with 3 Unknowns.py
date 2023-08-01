import numpy as np

def solve_3_equations_with_3_unknowns(a, b, c, d, e, f):
  """
  Solves 3 equations with 3 unknowns.

  Args:
    a: The coefficient of x in the first equation.
    b: The coefficient of y in the first equation.
    c: The coefficient of z in the first equation.
    d: The constant term in the first equation.
    e: The coefficient of x in the second equation.
    f: The constant term in the second equation.

  Returns:
    The solution vector x, y, z.
  """

  x = np.linalg.solve([[a, b, c], [e, f, 0], [0, 0, 1]], [d, f, 1])

  return x

if __name__ == "__main__":
  a = 1
  b = 2
  c = 3
  d = 4
  e = 5
  f = 6

  x = solve_3_equations_with_3_unknowns(a, b, c, d, e, f)
  print(x)
