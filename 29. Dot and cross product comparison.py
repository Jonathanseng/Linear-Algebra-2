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

def dot_and_cross_product_comparison():
  """Compares the dot and cross product."""
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  dot_product_result = dot_product(v1, v2)
  cross_product_result = cross_product(v1, v2)
  print("The dot product of v1 and v2 is:", dot_product_result)
  print("The cross product of v1 and v2 is:", cross_product_result)

if __name__ == "__main__":
  dot_and_cross_product_comparison()
