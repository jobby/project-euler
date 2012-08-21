def ur(n): return (2*n - 1) ** 2
def dr(n): return ur(n) - 6 * (n - 1)
def dl(n): return ur(n) - 4 * (n - 1)
def ul(n): return ur(n) - 2 * (n - 1)

print sum(map(lambda n: ur(n) + dr(n) + dl(n) + ul(n), range(2,502))) + 1

def q(n): return 16 * ( n ** 2 ) - 28 * n + 16

print sum(map(q, range(2,502))) + 1
