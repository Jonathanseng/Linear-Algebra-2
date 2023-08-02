def rref(matrix):
  """Computes the reduced row echelon form of a matrix."""
  n = len(matrix)
  for i in range(n):
    # Find the pivot element in column i.
    pivot_row = i
    for j in range(i + 1, n):
      if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
        pivot_row = j

    # Swap rows i and pivot_row.
    if pivot_row != i:
      matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

    # Make all other entries in column i equal to 0.
    for j in range(n):
      if j != i:
        factor = matrix[j][i] / matrix[i][i]
        for k in range(n):
          matrix[j][k] -= factor * matrix[i][k]

  return matrix

def basis(vectors):
  """Returns a basis for the set of vectors."""
  basis = []
  for vector in vectors:
    if not any(vector == b for b in basis):
      basis.append(vector)
  return basis

def is_basis(vectors):
  """Checks if a list of vectors is a basis."""
  for vector in vectors:
    if not any(vector == b for b in vectors):
      return False
  return True

def show_that_candidate_basis_does_span_C(matrix, candidate_basis):
  """Shows that the candidate basis does span C(A)."""
  rref_matrix = rref(matrix)
  basis_cols = basis(column_space(rref_matrix))
  for vector in candidate_basis:
    if vector not in basis_cols:
      raise ValueError("The candidate basis does not span C(A)")

if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  candidate_basis = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
  show_that_candidate_basis_does_span_C(matrix, candidate_basis)
