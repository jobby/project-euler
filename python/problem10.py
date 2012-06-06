import array

LIMIT = 2000000

cs = [0] * LIMIT

total = 0

for i in range(2,LIMIT):
    if cs[i] == 0:
        total += i
        for j in range(i,LIMIT,i):
            cs[j] = 1

print total