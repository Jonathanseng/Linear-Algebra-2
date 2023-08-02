def scaling(sx, sy):
  """
  Returns a matrix that scales points by sx and sy.

  Args:
    sx: The scale factor in the x direction.
    sy: The scale factor in the y direction.

  Returns:
    A matrix that scales points by sx and sy.
  """

  matrix = [[sx, 0], [0, sy]]
  return matrix


def reflection(axis):
  """
  Returns a matrix that reflects points across the given axis.

  Args:
    axis: The axis to reflect points across.

  Returns:
    A matrix that reflects points across the given axis.
  """

  if axis == "x":
    matrix = [[1, 0], [0, -1]]
  elif axis == "y":
    matrix = [[-1, 0], [0, 1]]
  else:
    raise ValueError("Invalid axis.")

  return matrix


if __name__ == "__main__":
  print(scaling(2, 3))
  print(reflection("x"))
