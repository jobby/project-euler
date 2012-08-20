fibs = [1,1]
i = 1
while(len(str(fibs[i])) < 1000):
    fibs.append(fibs[i] + fibs[i-1])
    i = i + 1
print i + 1
