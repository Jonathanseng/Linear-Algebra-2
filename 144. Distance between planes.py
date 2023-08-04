import numpy as np

def distance_between_planes(normal_vector_1, d_1, normal_vector_2, d_2):
  """
  Calculates the distance between two planes.
  """
  distance = np.linalg.norm(normal_vector_1 - normal_vector_2)
  return distance * np.linalg.norm(normal_vector_1)

def distance_between_planes_example():
  """
  Example of the distance between planes.
  """
  normal_vector_1 = np.array([1, 2, 3])
  d_1 = 4
  normal_vector_2 = np.array([1, 2, 3])
  d_2 = 5
  print("Distance between planes:")
  print(distance_between_planes(normal_vector_1, d_1, normal_vector_2, d_2))

if __name__ == '__main__':
  distance_between_planes_example()
