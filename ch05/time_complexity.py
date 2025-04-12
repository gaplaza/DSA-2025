def find_max(A):
  n = len(A)
  max = A[0]
  for i in range(n):
    if A[i] > max:
      max = A[i]
    return max