from __future__ import division
import math

def is_prime(x): 
    if math.sqrt(x).is_integer(): return False
    for i in range(2, int(math.ceil(math.sqrt(x)))):
        if x % i == 0:
            return False
    return True

def generate_nth_diagonal(n):
    n2 = 4 * n * n
    return [n2 - (4 * n) + 1,
            n2 - (6 * n) + 3,
            n2 - (8 * n) + 5,
            n2 - (10 * n ) + 7]

def count_primes(a):
    return len(filter(is_prime, a))

primes_seen = 0
for n in range(2, 100000):
    total = 1 + 4 * (n - 1)
    primes_seen += count_primes(generate_nth_diagonal(n))

    if primes_seen / total < 0.1:
        print (2 * n) - 1
        break
