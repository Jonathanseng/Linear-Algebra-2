import math


def projection(matrix, v):
  """
  Returns the projection of v onto the direction of matrix.

  Args:
    matrix: The matrix representing the direction of projection.
    v: The vector to project.

  Returns:
    The projection of v onto the direction of matrix.
  """

  v_unit = unit_vector(v)
  projection_length = dot(matrix, v_unit)
  projection_vector = projection_length * v_unit
  return projection_vector


def dot(matrix, v):
  """
  Returns the dot product of matrix and v.

  Args:
    matrix: The matrix.
    v: The vector.

  Returns:
    The dot product of matrix and v.
  """

  result = 0
  for i in range(len(matrix)):
    row = 0
    for j in range(len(matrix[0])):
      row += matrix[i][j] * v[j]
    result += row

  return result


def unit_vector(v):
  """
  Returns the unit vector in the direction of v.

  Args:
    v: The vector to find the unit vector of.

  Returns:
    The unit vector in the direction of v.
  """

  magnitude = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
  if magnitude == 0:
    return [0, 0, 0]
  else:
    return [v[0] / magnitude, v[1] / magnitude, v[2] / magnitude]


if __name__ == "__main__":
  matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
  v = [1, 2, 3]
  print(projection(matrix, v))
