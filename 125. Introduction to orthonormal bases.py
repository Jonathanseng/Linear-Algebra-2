import numpy as np

def orthonormal_basis(vectors):
  """
  Returns an orthonormal basis for the given vectors.

  Args:
    vectors: A list of NumPy arrays representing the vectors.

  Returns:
    The orthonormal basis.
  """

  # Normalize the vectors.
  normalized_vectors = np.array([vector / np.linalg.norm(vector) for vector in vectors])

  # Gram-Schmidt orthogonalize the vectors.
  for i in range(len(normalized_vectors)):
    for j in range(i):
      normalized_vectors[i] -= np.dot(normalized_vectors[i], normalized_vectors[j]) * normalized_vectors[j]

  return normalized_vectors

def main():
  # Define the vectors.
  vectors = np.array([[1, 0], [0, 1], [1, 1]])

  # Calculate the orthonormal basis.
  orthonormal_basis = orthonormal_basis(vectors)

  # Print the orthonormal basis.
  print(orthonormal_basis)

if __name__ == "__main__":
  main()
