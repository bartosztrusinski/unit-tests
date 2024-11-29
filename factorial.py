def factorial_iter(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def factorial_rec(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n < 2:
        return 1
    return factorial_rec(n - 1) * n

# list = [1, 2, 3, 4, 5, 6, 12, 18]
# print([factorial_iter(n) for n in list])
# print([factorial_rec(n) for n in list])
