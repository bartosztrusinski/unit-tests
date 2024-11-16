def factorial_iter(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def factorial_rec(n):
    if n < 3:
        return n
    return factorial_rec(n - 1) * n

list = [1, 2, 3, 4, 5, 6, 12, 18]
res_iter = [factorial_iter(n) for n in list]
res_rec = [factorial_rec(n) for n in list]

print(res_iter)
print(res_rec)
