def inverse_of_function(f, x):
  """Computes the inverse of a function f at x.

  Args:
    f: The function to be inverted.
    x: The input to the function.

  Returns:
    The output of the inverse function at x.
  """

  # Check if the function is invertible.
  if not f(f(x)) == x:
    raise ValueError("The function is not invertible.")

  # Compute the inverse of the function.
  inverse_function = lambda y: f(y)

  # Return the output of the inverse function at x.
  return inverse_function(x)

if __name__ == "__main__":
  # Define a function.
  def f(x):
    return x ** 2

  # Compute the inverse of the function.
  inverse_of_f = inverse_of_function(f, 4)

  # Print the inverse of the function.
  print(inverse_of_f)
