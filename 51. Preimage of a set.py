def preimage(set_a):
  """
  Returns the preimage of a set.

  Args:
    set_a: The set to find the preimage of.

  Returns:
    The preimage of set_a.
  """

  preimage = set()
  for x in range(len(set_a)):
    preimage.add(x for x in range(len(set_a)) if set_a[x] == x)
  return preimage


if __name__ == "__main__":
  set_a = [1, 2, 3, 4, 5]
  print(preimage(set_a))
