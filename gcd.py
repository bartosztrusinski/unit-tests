def gcd_iter(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_rec(a, b):
    if b == 0:
        return a
    return gcd_rec(b, a % b)

x, y = 20, 8

print(gcd_iter(x, y), gcd_rec(x, y))
