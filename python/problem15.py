import math

def binomial(x, y):
    return math.factorial(x) / (math.factorial(y) * math.factorial(x - y))

print binomial(40, 20)
