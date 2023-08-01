import numpy as np

def solve_3_variable_linear_equations(a, b, c, d, e, f):
  """
  Solves a system of 3-variable linear equations.

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

  x = (d - f) / (a - e)
  y = (f - b * x) / c
  z = (d - a * x) / b

  return x, y, z

if __name__ == "__main__":
  a = 1
  b = 2
  c = 3
  d = 4
  e = 5
  f = 6

  x, y, z = solve_3_variable_linear_equations(a, b, c, d, e, f)
  print(x, y, z)
