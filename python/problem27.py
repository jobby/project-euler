import math

primes = dict()

def is_prime(n):
    if n < 2: return False
    if n in primes:
        return primes[n]
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            primes[n] = False
            return False
        i += 1
    primes[n] = True
    return True

def q(a,b,n):
    return n ** 2 + a * n + b

maxp = 0
bestab = None

for a in range(-1000,1001):
    for b in range(2,1000):
        if not is_prime(b):
            continue
        n = 1
        while is_prime(q(a,b,n)):
            n += 1

        if n > maxp:
            maxp = n
            bestab = (a,b)

print maxp, bestab, bestab[0] * bestab[1]
