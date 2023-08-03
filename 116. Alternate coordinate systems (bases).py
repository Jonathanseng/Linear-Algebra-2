import numpy as np

def change_of_basis(v, old_basis, new_basis):
  """
  Performs change of basis from old_basis to new_basis.

  Args:
    v: Vector to transform.
    old_basis: Old basis.
    new_basis: New basis.

  Returns:
    Transformed vector.
  """

  new_v = np.dot(new_basis, np.dot(old_basis.T, v))
  return new_v

def main():
  old_basis = np.array([[1, 0], [0, 1]])
  new_basis = np.array([[1, 1], [1, -1]])
  v = np.array([1, 2])
  new_v = change_of_basis(v, old_basis, new_basis)
  print(new_v)

if __name__ == "__main__":
  main()
