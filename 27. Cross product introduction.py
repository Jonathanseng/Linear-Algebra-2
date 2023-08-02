def cross_product(v1, v2):
  """Computes the cross product of two vectors."""
  result = [
      v1[1] * v2[2] - v1[2] * v2[1],
      v1[2] * v2[0] - v1[0] * v2[2],
      v1[0] * v2[1] - v1[1] * v2[0],
  ]
  return result

if __name__ == "__main__":
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  cross_product_result = cross_product(v1, v2)
  print("The cross product of v1 and v2 is:", cross_product_result)
