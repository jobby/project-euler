import math
import operator

def curious(n):
    return n == sum(map(lambda x: math.factorial(int(x)), str(n)))

print sum(filter(curious, range(3,100000)))
