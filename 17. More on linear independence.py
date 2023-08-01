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

def main():
  """
  The main function.
  """

  vectors = np.array([[1, 2], [3, 4], [5, 6]])

  is_linearly_independent = is_linearly_independent(vectors)

  print(is_linearly_independent)

if __name__ == "__main__":
  main()
