import numpy as np

def distributive_property_of_matrix_products(A, B, C):
  """Computes the distributive property of matrix products.

  Args:
    A: The first matrix.
    B: The second matrix.
    C: The third matrix.

  Returns:
    The result of the distributive property.
  """

  # Compute the product of A and B.
  AB = np.dot(A, B)

  # Compute the product of B and C.
  BC = np.dot(B, C)

  # Compute the distributive property.
  distributive_property = AB + BC

  # Return the result.
  return distributive_property

if __name__ == "__main__":
  # Create three matrices.
  A = np.array([[1, 2], [3, 4]])
  B = np.array([[5, 6], [7, 8]])
  C = np.array([[9, 10], [11, 12]])

  # Compute the distributive property.
  distributive_property = distributive_property_of_matrix_products(A, B, C)

  # Print the distributive property.
  print(distributive_property)
