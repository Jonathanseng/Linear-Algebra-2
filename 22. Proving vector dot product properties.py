import math

def dot_product(v1, v2):
  """Computes the dot product of two vectors."""
  sum = 0
  for i in range(len(v1)):
    sum += v1[i] * v2[i]
  return sum

def vector_length(v):
  """Computes the length of a vector."""
  sum_of_squares = 0
  for i in range(len(v)):
    sum_of_squares += v[i] ** 2
  return sum_of_squares ** 0.5

def prove_dot_product_properties():
  """Proves the dot product properties."""
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  assert dot_product(v1, v2) == dot_product(v2, v1)
  assert dot_product(v1, v1) == vector_length(v1) ** 2
  assert dot_product(v1, [0, 0, 0]) == 0

if __name__ == "__main__":
  prove_dot_product_properties()
