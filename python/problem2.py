def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

total = 0
i = 0
f = fib(0)
while f < 4000000:
    if f % 2 == 0:
        total = total + f
    i = i + 1
    f = fib(i)

print total

cache = {0:0, 1:1}
def fib2(x):
    if x in cache:
        return cache[x]
    else:
        r = fib2(x-1) + fib2(x-2)
        cache[x] = r
        return r

print sum(filter(lambda x: x < 4000000 and x % 2 == 0,map(fib2, range(1,40))))