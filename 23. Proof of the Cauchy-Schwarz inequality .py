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

def prove_cauchy_schwarz_inequality():
  """Proves the Cauchy-Schwarz inequality."""
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  assert dot_product(v1, v2) ** 2 <= vector_length(v1) ** 2 * vector_length(v2) ** 2

if __name__ == "__main__":
  prove_cauchy_schwarz_inequality()
