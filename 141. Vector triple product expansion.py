import numpy as np

def vector_triple_product(a, b, c):
  """
  Calculates the vector triple product of a, b, and c.
  """
  return np.cross(a, np.cross(b, c))

def vector_triple_product_expansion_example():
  """
  Example of the vector triple product expansion.
  """
  a = np.array([1, 2, 3])
  b = np.array([4, 5, 6])
  c = np.array([7, 8, 9])
  print("Vector triple product:")
  print(vector_triple_product(a, b, c))
  print("Expanding the vector triple product:")
  print(a[0] * (b[1] * c[2] - b[2] * c[1]) + a[1] * (b[2] * c[0] - b[0] * c[2]) + a[2] * (b[0] * c[1] - b[1] * c[0]))

if __name__ == '__main__':
  vector_triple_product_expansion_example()
