import numpy as np

def point_distance_to_plane(point, normal_vector, d):
  """
  Calculates the distance from a point to a plane.
  """
  distance = np.dot(normal_vector, point) - d
  return distance / np.linalg.norm(normal_vector)

def point_distance_to_plane_example():
  """
  Example of the point distance to plane.
  """
  point = np.array([1, 2, 3])
  normal_vector = np.array([1, 2, 3])
  d = 4
  print("Distance from point to plane:")
  print(point_distance_to_plane(point, normal_vector, d))

if __name__ == '__main__':
  point_distance_to_plane_example()
