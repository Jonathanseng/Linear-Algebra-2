import math


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


def matrix_transformation(matrix, v):
  """
  Returns the result of applying the matrix transformation to v.

  Args:
    matrix: The matrix to apply the transformation to.
    v: The vector to apply the transformation to.

  Returns:
    The result of applying the matrix transformation to v.
  """

  result = []
  for i in range(len(matrix)):
    row = 0
    for j in range(len(matrix[0])):
      row += matrix[i][j] * v[j]
    result.append(row)

  return result


if __name__ == "__main__":
  v = [1, 2, 3]
  print(unit_vector(v))
  print(matrix_transformation([[1, 0, 0], [0, 1, 0], [0, 0, 1]], v))
