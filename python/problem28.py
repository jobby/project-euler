def q(n): return 16 * ( n ** 2 ) - 28 * n + 16

print sum(map(q, range(2,502))) + 1
