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

if __name__ == "__main__":
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  print("The dot product of v1 and v2 is:", dot_product(v1, v2))
  print("The length of v1 is:", vector_length(v1))
