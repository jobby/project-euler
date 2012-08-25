def valid(b,c,p):
    return ((p - b) ** 2) + (b ** 2) - (2 * c * (p - b)) == 0

def solutions(p):
    solutions = 0
    for b in range(1,p / 2):
        for c in range(b,p / 2):
            if valid(b,c,p) and p-b-c > 0:
                solutions += 1

    return solutions / 2

largest = 0
maxp = 0
for p in range(1,1001):
    s = solutions(p)
    if s > largest:
        largest = s
        maxp = p

print maxp
