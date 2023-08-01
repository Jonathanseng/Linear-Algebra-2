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

def main():
  """
  The main function.
  """

  v1 = create_vector(1, 2, 3)
  v2 = create_vector(4, 5, 6)

  sum_vector = add_vectors(v1, v2)

  print(sum_vector)

if __name__ == "__main__":
  main()
