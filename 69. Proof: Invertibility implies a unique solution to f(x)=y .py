def proof_invertibility_implies_unique_solution(f, y):
  """Proof that invertibility implies a unique solution to f(x)=y.

  Args:
    f: The function to be inverted.
    y: The output of the function.

  Returns:
    True if the function is invertible and there is a unique solution to f(x)=y,
    False otherwise.
  """

  # Check if the function is invertible.
  if not f(f(y)) == y:
    return False

  # Set x to be the solution to f(x)=y.
  x = f(y)

  # Check if there is another solution to f(x)=y.
  if f(x) != y:
    return False

  # Return True if the function is invertible and there is a unique solution to f(x)=y.
  return True

if __name__ == "__main__":
  # Define a function.
  def f(x):
    return x ** 2

  # Test the function.
  if proof_invertibility_implies_unique_solution(f, 4):
    print("The function is invertible and there is a unique solution to f(x)=4.")
  else:
    print("The function is not invertible or there is not a unique solution to f(x)=4.")
