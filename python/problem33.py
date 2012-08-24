from __future__ import division

def curious(n, d):
    if n % 10 == 0  or d % 10 == 0:
        return False
    if n // 10 == d % 10: 
        return (n % 10) / (d // 10) == n / d
    elif n % 10 == d // 10:
       return (n // 10) / (d % 10) == n / d
    else:
        return False

p = 1
for numerator in range(10,100):
    for denominator in range(numerator + 1, 100):
        if curious(numerator, denominator):
            p *= (numerator / denominator)

print p




