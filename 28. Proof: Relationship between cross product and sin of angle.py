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

def cross_product(v1, v2):
  """Computes the cross product of two vectors."""
  result = [
      v1[1] * v2[2] - v1[2] * v2[1],
      v1[2] * v2[0] - v1[0] * v2[2],
      v1[0] * v2[1] - v1[1] * v2[0],
  ]
  return result

def proof_relationship_between_cross_product_and_sin_of_angle():
  """Proves the relationship between the cross product and the sine of an angle."""
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  l1 = vector_length(v1)
  l2 = vector_length(v2)
  sin_theta = dot_product(v1, v2) / (l1 * l2)
  cross_product_result = cross_product(v1, v2)
  assert abs(cross_product_result[0]) == abs(sin_theta * l1 * l2)

if __name__ == "__main__":
  proof_relationship_between_cross_product_and_sin_of_angle()
