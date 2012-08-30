def is_perm(x, y):
    return set(str(x)) == set(str(y))

for i in range(100000, 166667):
    perm = True
    for m in range(2,7):
        perm = perm and is_perm(i, i * m)
    if perm:
        print i
        break
