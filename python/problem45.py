def is_pent(n):
    r = math.sqrt((24 * n) + 1)
    return r.is_integer() and r % 6 == 5

def hex(n):
    return n*((2*n) - 1)

h = 144

while not is_pent(hex(h)):
    h += 1

print hex(h)
