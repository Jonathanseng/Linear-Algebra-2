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

def define_plane_with_point_and_normal_vector(point, normal_vector):
  """Defines a plane in R3 with a point and normal vector."""
  d = -dot_product(normal_vector, point)
  return [normal_vector[0], normal_vector[1], normal_vector[2], d]

if __name__ == "__main__":
  point = [1, 2, 3]
  normal_vector = [4, 5, 6]
  plane = define_plane_with_point_and_normal_vector(point, normal_vector)
  print("The equation of the plane is:", plane)
