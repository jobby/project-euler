def isprime(x):
    for i in range(2, int(math.ceil(math.sqrt(x)))):
        if x % i == 0:
            return False
    return True

def factors(x):
    if x == 1: return [1]
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            r = factors(x/i)
            r.append(i)
            return r
        i += 1
    return [x]

x = 600851475143
print filter(isprime, factors(x))[0]