def sum_of_linear_transformations(T1, T2):
  """
  Returns the sum of two linear transformations.

  Args:
    T1: The first linear transformation.
    T2: The second linear transformation.

  Returns:
    The sum of T1 and T2.
  """

  def sum_of_transformations(v):
    return T1(v) + T2(v)

  return sum_of_transformations


def scalar_multiple_of_linear_transformation(c, T):
  """
  Returns the scalar multiple of a linear transformation.

  Args:
    c: The scalar.
    T: The linear transformation.

  Returns:
    The scalar multiple of T.
  """

  def scalar_multiple_of_transformation(v):
    return c * T(v)

  return scalar_multiple_of_transformation


if __name__ == "__main__":
  T1 = lambda v: v * 2
  T2 = lambda v: v + 1

  print(sum_of_linear_transformations(T1, T2)(3))
  print(scalar_multiple_of_linear_transformation(2, T1)(3))
