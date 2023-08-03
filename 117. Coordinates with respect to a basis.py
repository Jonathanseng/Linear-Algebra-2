import numpy as np

def coordinates(v, basis):
  """
  Calculates the coordinates of v with respect to basis.

  Args:
    v: Vector to calculate coordinates for.
    basis: Basis vectors.

  Returns:
    Coordinates of v with respect to basis.
  """

  coordinates = np.dot(v, basis.T)
  return coordinates

def main():
  basis = np.array([[1, 0], [0, 1]])
  v = np.array([1, 2])
  coordinates = coordinates(v, basis)
  print(coordinates)

if __name__ == "__main__":
  main()
