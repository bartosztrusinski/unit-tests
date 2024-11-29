def fib_iter(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_rec(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

# list = [0, 1, 2, 3, 4, 5, 12, 30]
# print([fib_iter(n) for n in list])
# print([fib_rec(n) for n in list])
