import math


def rotation(angle):
  """
  Returns a matrix that rotates points by angle radians.

  Args:
    angle: The angle to rotate points by in radians.

  Returns:
    A matrix that rotates points by angle radians.
  """

  c = math.cos(angle)
  s = math.sin(angle)
  matrix = [[c, -s], [s, c]]
  return matrix


if __name__ == "__main__":
  print(rotation(math.pi / 4))
