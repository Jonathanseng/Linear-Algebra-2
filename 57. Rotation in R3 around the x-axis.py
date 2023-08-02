import math


def rotation_x(angle):
  """
  Returns a matrix that rotates points around the x-axis by angle radians.

  Args:
    angle: The angle to rotate points by in radians.

  Returns:
    A matrix that rotates points around the x-axis by angle radians.
  """

  c = math.cos(angle)
  s = math.sin(angle)
  matrix = [[1, 0, 0], [0, c, -s], [0, s, c]]
  return matrix


if __name__ == "__main__":
  print(rotation_x(math.pi / 4))
