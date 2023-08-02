def preimage(f, x):
  """
  Returns the preimage of a function.

  Args:
    f: The function to find the preimage of.
    x: The element to find the preimage of.

  Returns:
    The preimage of x under f.
  """

  preimage = set()
  for y in range(f(f(x))):
    if f(y) == x:
      preimage.add(y)
  return preimage


def kernel(f):
  """
  Returns the kernel of a function.

  Args:
    f: The function to find the kernel of.

  Returns:
    The kernel of f.
  """

  kernel = set()
  for x in range(f(f(0))):
    if f(x) == 0:
      kernel.add(x)
  return kernel


if __name__ == "__main__":
  f = lambda x: x * x
  print(preimage(f, 4))
  print(kernel(f))
