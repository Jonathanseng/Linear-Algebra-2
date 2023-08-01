import numpy as np

def is_linearly_independent(vectors):
  """
  Returns whether a set of vectors are linearly independent.

  Args:
    vectors: The set of vectors.

  Returns:
    True if the vectors are linearly independent, False otherwise.
  """

  if len(vectors) == 1:
    return True

  determinant = np.linalg.det(vectors)

  if determinant == 0:
    return False
  else:
    return True

def span(vectors):
  """
  Returns the span of a set of vectors.

  Args:
    vectors: The set of vectors.

  Returns:
    The span of the vectors.
  """

  span = np.array([linear_combination(vectors, a, b)
                    for a in range(-10, 11)
                    for b in range(-10, 11)])

  return span

def main():
  """
  The main function.
  """

  vectors = np.array([[1, 2], [3, 4], [5, 6]])

  is_linearly_independent = is_linearly_independent(vectors)
  span = span(vectors)

  print(is_linearly_independent)
  print(span)

if __name__ == "__main__":
  main()
