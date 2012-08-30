import math
import itertools

ps = {1:False}

def is_prime(n):
    if n in ps: return ps[n]
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            ps[n] = False
            return False
        i += 1
    ps[n] = True
    return True

def primes_upto(limit):
    return filter(is_prime, range(2,limit))

def squares_upto(limit):
    return map(lambda n: n ** 2,list(itertools.takewhile(lambda x: x ** 2 <= limit, itertools.count(1))))

for i in range(3,1000000,2):
    found = False
    if is_prime(i): continue
    for p in primes_upto(i):
        for s in squares_upto((i - p) / 2):
            if p + ( 2 * s ) == i:
                #print "%d = %d + 2 * %d ** 2" % (i, p, s)
                found = True
                break

        if found: break


    if not found:
        print i
        break
