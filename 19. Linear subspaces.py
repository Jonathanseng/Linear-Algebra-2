import numpy as np

def is_linear_subspace(vectors):
  """
  Returns whether a set of vectors form a linear subspace.

  Args:
    vectors: The set of vectors.

  Returns:
    True if the vectors form a linear subspace, False otherwise.
  """

  if not is_linearly_independent(vectors):
    return False

  for vector in vectors:
    if not np.all(np.linalg.lstsq(vectors, vector)[0] == 1):
      return False

  return True

def main():
  """
  The main function.
  """

  vectors = np.array([[1, 2], [3, 4], [5, 6]])

  is_linear_subspace = is_linear_subspace(vectors)

  print(is_linear_subspace)

if __name__ == "__main__":
  main()
