from time import time
start = time()

def tri(n):
    return n * (n + 1) / 2
def squ(n):
    return n * n
def pen(n):
    return n * ((3 * n) - 1) / 2
def hex(n):
    return n * ((2 * n) - 1)
def hep(n):
    return n * ((5 * n) - 3) / 2
def oct(n):
    return n * ((3 * n) - 2)

def gen(f):
    return filter(lambda x: x > 1000 and x < 10000, map(f, range(1,150)))

def friends(x, y):
    return x % 100 == y / 100

layers = map(gen, [tri, squ, pen, hex, hep, oct])

def go(number, layers_used, sofar):
    if len(layers_used) == 6:
        if friends(number, sofar[0]):
            print sofar, number
            print sum(sofar) + number
            print '%f ms' % ((time() - start) * 100)
    else:
        for l in range(0, 6):
            if l not in layers_used:
                potential_next = [x for x in layers[l] if friends(number, x)]
#                c = list(sofar)
#                c.append(number)
#                new_layers = list(layers_used)
#                new_layers.append(l)
                for p in potential_next:
                    layers_used.append(l)
                    sofar.append(number)
                    go(p, layers_used, sofar)
                    sofar.remove(number)
                    layers_used.remove(l)

for i in layers[5]:
    go(i, [5], [])

print "done"
