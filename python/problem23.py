def divisors(x):
    ret = [1]
    for i in range (2, int(math.floor(math.sqrt(x))) + 1):
        if x % i == 0:
            ret.append(i)
            if(i * i != x ):
                ret.append(x / i)
    return ret

def abundant(x):
    return sum(divisors(x)) > x

abs = filter(abundant, range(12, 28124))

ab_sums = []
for i in abs:
    for j in abs:
        ab_sums.append(i + j)

ab_set = set(ab_sums)

print filter(lambda x: not x in ab_set, range(20,31))
print filter(lambda x: x in ab_set, range(20,31))

print sum(filter(lambda x: not x in ab_set, range(1,28123)))