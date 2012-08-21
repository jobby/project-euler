import math

def is_prime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def decimals(dividend, divisor, digits):
    r = []
    while len(r) < digits:
        if dividend == divisor:
            return r
        elif dividend < divisor:
            dividend *= 10
            r.append(0)
        else:
            r.append(dividend / divisor)
            dividend = dividend % divisor
            dividend *= 10
    return r

def maxperiod(decs,n):
    m = len(decs) / 2
    while n <= m:
        if decs[0:n] == decs[n:n*2]:
            return n
        n += 1
    return n

primes = filter(is_prime, range(2,1001))

# for prime p, repeating decimal will have period at most p - 1, so only check these

maxp = 0
maxn = 0

for p in primes:
    decs = decimals(1, p, ((p-1) * 2) + 1)
    decs = decs[1:]
    l = maxperiod(decs, int(math.log10(p)))
    if l > maxp:
        maxp = l
        maxn = p

print maxn
