def gcd_iter(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Both inputs must be non-negative.")
    
    while b:
        a, b = b, a % b
    return a

def gcd_rec(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Both inputs must be non-negative.")
    
    if b == 0:
        return a
    return gcd_rec(b, a % b)

# x, y = 20, 8
# print(gcd_iter(x, y), gcd_rec(x, y))
