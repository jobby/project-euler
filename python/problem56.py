def digitsum(n):
    return sum(map(lambda s:int(s), str(n)))

print max(map(digitsum, [(a ** b) for a in range(1,100) for b in range(1,100)]))
