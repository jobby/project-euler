import math

def pent(n):
    return n * ((3 * n) - 1) / 2

def is_pent(n):
    r = math.sqrt((24 * n) + 1)
    return r.is_integer() and r % 6 == 5

cs = []

for x in range(1,2500):
    for y in range(1, x):
        px = pent(x)
        py = pent(y)
        cs.append((px, py, abs(px-py), px + py))

cs = sorted(cs, key = lambda x: x[2])

for c in cs:
    if is_pent(c[3]) and is_pent(c[2]):
        print c[2]
        break

