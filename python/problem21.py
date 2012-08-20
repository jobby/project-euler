def divisors(n):
    return filter(lambda x: n % x == 0, range(1,n/2 + 1))

def amicable(a):
    aprime = sum(divisors(a))
    b = sum(divisors(aprime))
    return a == b and a != aprime

print sum(filter(amicable, range(1,10001)))
