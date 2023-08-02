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

def angle_between_vectors(v1, v2):
  """Computes the angle between two vectors."""
  dot = dot_product(v1, v2)
  l1 = vector_length(v1)
  l2 = vector_length(v2)
  angle = math.acos(dot / (l1 * l2))
  return angle

if __name__ == "__main__":
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  angle = angle_between_vectors(v1, v2)
  print("The angle between v1 and v2 is:", angle)
