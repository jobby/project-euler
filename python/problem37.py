import math

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

def checktrunc(n):
    t = is_prime(n) and not "0" in str(n)
    if not t: return t

    for i in range(1,len(str(n))):
        t &= is_prime(int(str(n)[i:]))
        t &= is_prime(int(str(n)[:-i]))

    return t

print sum(filter(checktrunc, range(9, 1000000, 2)))


