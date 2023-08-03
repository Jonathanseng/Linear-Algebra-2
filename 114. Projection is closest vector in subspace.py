import numpy as np

def projection(v, u):
  """
  Projects vector v onto subspace spanned by u.

  Args:
    v: Vector to project.
    u: Vector spanning the subspace.

  Returns:
    Projection of v onto subspace spanned by u.
  """

  projection_coefficient = np.dot(v, u) / np.dot(u, u)
  return projection_coefficient * u

def main():
  v = np.array([1, 2, 3])
  u = np.array([2, 0, 0])
  projection = projection(v, u)
  print(projection)

if __name__ == "__main__":
  main()
