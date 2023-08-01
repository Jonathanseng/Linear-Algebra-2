import numpy as np

def is_linearly_independent(v1, v2):
  """
  Returns whether two vectors are linearly independent.

  Args:
    v1: The first vector.
    v2: The second vector.

  Returns:
    True if the vectors are linearly independent, False otherwise.
  """

  if np.linalg.det([v1, v2]) == 0:
    return False
  else:
    return True

def main():
  """
  The main function.
  """

  v1 = np.array([1, 2])
  v2 = np.array([3, 4])

  is_linearly_independent = is_linearly_independent(v1, v2)

  print(is_linearly_independent)

if __name__ == "__main__":
  main()
