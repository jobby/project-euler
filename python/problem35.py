import math

ps = {}

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

def checkcircles(n):
    if '0' in str(n):
        return False
    t = True
    for i in range(0, int(math.ceil(math.log10(n)))):
        t &= is_prime(n)
        n = int(str(n)[1:] + str(n)[0:1])
    return t

print len(filter(checkcircles, range(2, 1000000)))
