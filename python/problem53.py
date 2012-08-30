import math

def choose(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

total = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if choose(n, r) > 1000000:
            total += 1

print total
