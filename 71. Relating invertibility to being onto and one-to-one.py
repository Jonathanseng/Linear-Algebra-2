def relate_invertibility_to_onto_and_one_to_one(f):
  """Relates invertibility to being onto and one-to-one.

  Args:
    f: The function to be checked.

  Returns:
    A tuple of three boolean values, representing whether the function is
    invertibe, onto, and one-to-one.
  """

  is_invertible = True
  is_onto = True
  is_one_to_one = True

  for y in f.codomain:
    # Check if there is an x in the domain such that f(x)=y.
    x = None
    for x_ in f.domain:
      if f(x_) == y:
        x = x_
        break

    # If there is no x in the domain such that f(x)=y, then the function is not onto.
    if x is None:
      is_onto = False
      break

  for x1 in f.domain:
    for x2 in f.domain:
      # Check if f(x1)=f(x2) implies x1=x2.
      if f(x1) == f(x2) and x1 != x2:
        is_one_to_one = False
        break

  if not is_one_to_one:
    is_invertible = False

  return is_invertible, is_onto, is_one_to_one

if __name__ == "__main__":
  # Define a function.
  def f(x):
    return x ** 2

  # Check the properties of the function.
  is_invertible, is_onto, is_one_to_one = relate_invertibility_to_onto_and_one_to_one(f)

  # Print the properties of the function.
  print("The function is invertible:", is_invertible)
  print("The function is onto:", is_onto)
  print("The function is one-to-one:", is_one_to_one)
