import numpy as np

def simplify_conditions_for_invertibility(A):
  """Simplifies the conditions for invertibility of a matrix A.

  Args:
    A: The matrix A.

  Returns:
    A tuple of three boolean values, representing whether the matrix is
    invertibe, onto, and one-to-one.
  """

  is_invertible, is_onto, is_one_to_one = relate_invertibility_to_onto_and_one_to_one(A)

  # If the matrix is not invertible, then it is not onto or one-to-one.
  if not is_invertible:
    is_onto = False
    is_one_to_one = False

  return is_invertible, is_onto, is_one_to_one

if __name__ == "__main__":
  # Create a matrix A.
  A = np.array([[1, 2], [3, 4]])

  # Simplify the conditions for invertibility of A.
  is_invertible, is_onto, is_one_to_one = simplify_conditions_for_invertibility(A)

  # Print the conditions.
  print("The matrix A is invertible:", is_invertible)
  print("The matrix A is onto:", is_onto)
  print("The matrix A is one-to-one:", is_one_to_one)
