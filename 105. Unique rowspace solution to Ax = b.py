import numpy as np

def unique_rowspace_solution(matrix, vector):
  """
  Calculates the unique rowspace solution to Ax = b.

  Args:
    matrix: The matrix.
    vector: The vector.

  Returns:
    The unique rowspace solution to Ax = b.
  """

  if np.linalg.matrix_rank(matrix) != np.linalg.matrix_rank(np.append(matrix, vector, axis=1)):
    return None
  else:
    return np.linalg.lstsq(matrix, vector, rcond=-1)[0]

def main():
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  vector = [1, 2, 3]
  solution = unique_rowspace_solution(matrix, vector)
  print(solution)

if __name__ == "__main__":
  main()
