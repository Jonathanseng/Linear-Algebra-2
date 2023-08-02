def surjective_function(f, domain, codomain):
  """Checks if a function is surjective.

  Args:
    f: The function to be checked.
    domain: The domain of the function.
    codomain: The codomain of the function.

  Returns:
    True if the function is surjective, False otherwise.
  """

  for y in codomain:
    # Check if there is an x in the domain such that f(x)=y.
    x = None
    for x_ in domain:
      if f(x_) == y:
        x = x_
        break

    # If there is no x in the domain such that f(x)=y, then the function is not surjective.
    if x is None:
      return False

  # The function is surjective.
  return True

def injective_function(f, domain):
  """Checks if a function is injective.

  Args:
    f: The function to be checked.
    domain: The domain of the function.

  Returns:
    True if the function is injective, False otherwise.
  """

  for x1 in domain:
    for x2 in domain:
      # Check if f(x1)=f(x2) implies x1=x2.
      if f(x1) == f(x2) and x1 != x2:
        return False

  # The function is injective.
  return True

if __name__ == "__main__":
  # Define a function.
  def f(x):
    return x ** 2

  # Check if the function is surjective.
  if surjective_function(f, range(10), range(100)):
    print("The function is surjective.")
  else:
    print("The function is not surjective.")

  # Check if the function is injective.
  if injective_function(f, range(10)):
    print("The function is injective.")
  else:
    print("The function is not injective.")
