def ispan(a,b,p):
    s = str(a) + str(b) + str(p)
    return not( len(s) != 9 or len(set(s)) != 9 or '0' in s )

ts = []
for a in range(1,2000):
    for b in range(1,2000):
        if ispan(a, b, a*b):
            ts.append(a*b)

print sum(set(ts))
