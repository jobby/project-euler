s = ""
for i in range(0,200000):
    s += (str(i))

t = 1
for n in range(0,7):
    t *= int(s[10 ** n])

print t
