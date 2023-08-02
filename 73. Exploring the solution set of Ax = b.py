import numpy as np

def explore_solution_set(A, b):
  """Explores the solution set of Ax = b.

  Args:
    A: The matrix A.
    b: The vector b.

  Returns:
    The list of all solutions to Ax = b.
  """

  # Check if the matrix A is invertible.
  if not np.linalg.det(A) == 0:
    # The matrix A is invertible, so there is a unique solution to Ax = b.
    x = np.linalg.solve(A, b)
    return [x]
  else:
    # The matrix A is not invertible, so there are infinitely many solutions to Ax = b.
    solutions = []
    for c in range(len(b)):
      x = np.zeros(len(A))
      x[c] = 1
      solutions.append(x)
    return solutions

if __name__ == "__main__":
  # Create a matrix A and a vector b.
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6])

  # Explore the solution set of Ax = b.
  solutions = explore_solution_set(A, b)

  # Print the solutions.
  for solution in solutions:
    print(solution)
