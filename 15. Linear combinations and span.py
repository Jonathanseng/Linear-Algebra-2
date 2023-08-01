import numpy as np

def linear_combination(v1, v2, a, b):
  """
  Returns the linear combination of two vectors.

  Args:
    v1: The first vector.
    v2: The second vector.
    a: The coefficient of the first vector.
    b: The coefficient of the second vector.

  Returns:
    The linear combination of the two vectors.
  """

  linear_combination = a * v1 + b * v2

  return linear_combination

def span(v1, v2):
  """
  Returns the span of two vectors.

  Args:
    v1: The first vector.
    v2: The second vector.

  Returns:
    The span of the two vectors.
  """

  span = np.array([linear_combination(v1, v2, a, b)
                    for a in range(-10, 11)
                    for b in range(-10, 11)])

  return span

def main():
  """
  The main function.
  """

  v1 = np.array([1, 2])
  v2 = np.array([3, 4])

  span = span(v1, v2)

  print(span)

if __name__ == "__main__":
  main()
