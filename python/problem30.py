def sum_powers(n):
    return n == sum(map(lambda x: x** 5, map(int,str(n))))

print sum(filter(sum_powers, range(2,1000000)))
