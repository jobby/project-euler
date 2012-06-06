import math

def num_divisors(x):
    ret = 1
    for i in range (2, int(math.floor(math.sqrt(x))) + 1):
        if x % i == 0:
            ret = ret + 1
            if(i * i != x ):
                ret = ret + 1
    return ret



tri = 1
for i in range(2,1000000):
    tri += i
    if num_divisors2(tri) > 500:
        break

print tri