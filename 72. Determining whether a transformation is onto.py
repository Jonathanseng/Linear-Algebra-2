def is_onto_transformation(transformation, codomain):
  """Checks if a transformation is onto.

  Args:
    transformation: The transformation to be checked.
    codomain: The codomain of the transformation.

  Returns:
    True if the transformation is onto, False otherwise.
  """

  for y in codomain:
    # Check if there is an x in the domain such that transformation(x)=y.
    x = None
    for x_ in transformation.domain:
      if transformation(x_) == y:
        x = x_
        break

    # If there is no x in the domain such that transformation(x)=y, then the transformation is not onto.
    if x is None:
      return False

  # The transformation is onto.
  return True

if __name__ == "__main__":
  # Define a transformation.
  def transformation(x):
    return x ** 2

  # Check if the transformation is onto.
  if is_onto_transformation(transformation, range(100)):
    print("The transformation is onto.")
  else:
    print("The transformation is not onto.")
