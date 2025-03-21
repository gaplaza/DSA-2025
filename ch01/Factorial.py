def factorial_iter(n):
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result
  
def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recur(n - 1)