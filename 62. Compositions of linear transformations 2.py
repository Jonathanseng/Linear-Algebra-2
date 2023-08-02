import math


def composition_matrix(T1, T2):
  """
  Returns the matrix that represents the composition of T1 and T2.

  Args:
    T1: The first linear transformation.
    T2: The second linear transformation.

  Returns:
    The matrix that represents the composition of T1 and T2.
  """

  matrix = []
  for i in range(len(T1)):
    row = []
    for j in range(len(T2[0])):
      dot_product = 0
      for k in range(len(T1[0])):
        dot_product += T1[i][k] * T2[k][j]
      row.append(dot_product)
    matrix.append(row)

  return matrix


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
  matrix = composition_matrix(T1, T2)
  v = [1, 2, 3]
  print(matrix_transformation(matrix, v))
