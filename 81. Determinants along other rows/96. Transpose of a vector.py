def transpose(vector):
  """
  Calculates the transpose of a vector.

  Args:
    vector: A 1D list of numbers.

  Returns:
    The transpose of the vector.
  """

  transposed_vector = []
  for i in range(len(vector)):
    transposed_vector.append([vector[i]])
  return transposed_vector

if __name__ == "__main__":
  vector = [1, 2, 3]
  transposed_vector = transpose(vector)
  print(transposed_vector)
