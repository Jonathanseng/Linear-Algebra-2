import numpy as np

def create_vector(x, y, z):
  """
  Creates a vector.

  Args:
    x: The x-coordinate of the vector.
    y: The y-coordinate of the vector.
    z: The z-coordinate of the vector.

  Returns:
    The vector.
  """

  vector = np.array([x, y, z])

  return vector

def add_vectors(v1, v2):
  """
  Adds two vectors.

  Args:
    v1: The first vector.
    v2: The second vector.

  Returns:
    The sum of the two vectors.
  """

  sum_vector = v1 + v2

  return sum_vector

def dot_product(v1, v2):
  """
  Calculates the dot product of two vectors.

  Args:
    v1: The first vector.
    v2: The second vector.

  Returns:
    The dot product of the two vectors.
  """

  dot_product = np.dot(v1, v2)

  return dot_product

def main():
  """
  The main function.
  """

  v1 = create_vector(1, 2, 3)
  v2 = create_vector(4, 5, 6)

  sum_vector = add_vectors(v1, v2)
  dot_product = dot_product(v1, v2)

  print(sum_vector)
  print(dot_product)

if __name__ == "__main__":
  main()
