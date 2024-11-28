def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Unsupported types for add()")
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


x = 12
y = 5

# print(add(x,y), subtract(x,y), multiply(x,y), divide(x,y))
