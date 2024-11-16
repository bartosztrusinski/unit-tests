def fib_iter(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

list = [0, 1, 2, 3, 4, 5, 12, 30]
res_iter = [fib_iter(n) for n in list]
res_rec = [fib_rec(n) for n in list]

print(res_iter)
print(res_rec)
