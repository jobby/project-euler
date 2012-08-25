def ispan(s):
    return not( len(s) != 9 or len(set(s)) != 9 or '0' in s )

largest = 0
for i in range(2, 10000):
    for r in range(2,10):
        t = ""
        for n in range(1, r + 1):
            t += str(i * n)
        if ispan(t) and t > largest:
            largest = t

print largest 
