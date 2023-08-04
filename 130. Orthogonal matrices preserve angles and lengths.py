import numpy as np

def orthogonal_matrix(vectors):
  """
  Returns an orthogonal matrix for the given vectors.

  Args:
    vectors: A list of NumPy arrays representing the vectors.

  Returns:
    The orthogonal matrix.
  """

  # Normalize the vectors.
  normalized_vectors = np.array([vector / np.linalg.norm(vector) for vector in vectors])

  # Gram-Schmidt orthogonalize the vectors.
  for i in range(len(normalized_vectors)):
    for j in range(i):
      normalized_vectors[i] -= np.dot(normalized_vectors[i], normalized_vectors[j]) * normalized_vectors[j]

  # Create the orthogonal matrix.
  orthogonal_matrix = np.array(normalized_vectors).T

  return orthogonal_matrix

def main():
  # Define the vectors.
  vectors = np.array([[1, 0], [0, 1], [1, 1]])

  # Calculate the orthogonal matrix.
  orthogonal_matrix = orthogonal_matrix(vectors)

  # Print the orthogonal matrix.
  print(orthogonal_matrix)

if __name__ == "__main__":
  main()
