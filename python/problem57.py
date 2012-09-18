c = 0
n = [1,2]
for i in range(2,1001):
    # add 2
    n[0] = n[0] + n[1] * 2
    # take reciprocal 
    n[0], n[1] = n[1], n[0]
    # check 1 plus n
    if len(str(n[0] + n[1])) > len(str(n[1])): c += 1

print c
