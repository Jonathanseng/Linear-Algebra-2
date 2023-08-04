import numpy as np

def normal_vector_from_plane_equation(a, b, c, d):
  """
  Calculates the normal vector from the plane equation.
  """
  normal_vector = np.array([a, b, c])
  normal_vector /= np.linalg.norm(normal_vector)
  return normal_vector

def normal_vector_from_plane_equation_example():
  """
  Example of the normal vector from plane equation.
  """
  a = 1
  b = 2
  c = 3
  d = 4
  print("Normal vector:")
  print(normal_vector_from_plane_equation(a, b, c, d))

if __name__ == '__main__':
  normal_vector_from_plane_equation_example()
