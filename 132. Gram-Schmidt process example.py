import numpy as np

def gram_schmidt(A):
  """
  Applies the Gram-Schmidt method to A and returns Q and R, so that
    Q * R = A
  """
  Q = []
  R = np.zeros_like(A)
  for i in range(A.shape[1]):
    v = A[:, i]
    for j in range(i):
      proj = np.dot(Q[j], v)
      v -= proj * Q[j]
    R[i, i] = np.linalg.norm(v)
    Q.append(v / R[i, i])
  return Q, R

if __name__ == '__main__':
  A = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]])
  Q, R = gram_schmidt(A)
  print(Q)
  print(R)
