import numpy as np

def represent_vector(vector, subspace):
  """
  Represents a vector in $\mathbb{R}^n$ using subspace members.

  Args:
    vector: The vector.
    subspace: The subspace.

  Returns:
    The representation of the vector in the subspace.
  """

  projection = np.dot(vector, subspace)
  representation = []
  for i in range(len(subspace)):
    representation.append(projection[i] * subspace[i])
  return representation

def main():
  vector = [1, 2, 3]
  subspace = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
  representation = represent_vector(vector, subspace)
  print(representation)

if __name__ == "__main__":
  main()
