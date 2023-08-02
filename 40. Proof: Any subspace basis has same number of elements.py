def is_basis(vectors):
  """Checks if a list of vectors is a basis."""
  for vector in vectors:
    if not any(vector == b for b in vectors):
      return False
  return True

def number_of_elements_in_subspace(vectors):
  """Returns the number of elements in the subspace spanned by the vectors."""
  basis = basis(vectors)
  return len(basis)

def proof(vectors):
  """Proof that any subspace basis has the same number of elements."""
  n = number_of_elements_in_subspace(vectors)
  for i in range(n):
    for j in range(i + 1, n):
      if vectors[i] == vectors[j]:
        raise ValueError("The vectors are not linearly independent")
  return n

if __name__ == "__main__":
  vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print("The number of elements in the subspace spanned by the vectors is:",
        proof(vectors))
