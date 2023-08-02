import math

def vector_length(v):
  """Computes the length of a vector."""
  sum_of_squares = 0
  for i in range(len(v)):
    sum_of_squares += v[i] ** 2
  return sum_of_squares ** 0.5

def vector_triangle_inequality():
  """Proves the vector triangle inequality."""
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  v3 = [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]
  assert vector_length(v3) <= vector_length(v1) + vector_length(v2)

if __name__ == "__main__":
  vector_triangle_inequality()
