import math


def composition(T1, T2, v):
  """
  Returns the composition of T1 and T2 applied to v.

  Args:
    T1: The first linear transformation.
    T2: The second linear transformation.
    v: The vector to apply the transformations to.

  Returns:
    The composition of T1 and T2 applied to v.
  """

  v_prime = T1(v)
  return T2(v_prime)


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
  T1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
  T2 = [[2, 0, 0], [0, 3, 0], [0, 0, 4]]
  v = [1, 2, 3]
  print(composition(T1, T2, v))
