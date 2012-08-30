import itertools
import math

def prime_sieve(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

ps = prime_sieve(10000)

def get_primes_between(m,n):
    i = 0
    while ps[i] <= m:
        i += 1
    
    j = 0
    while ps[j] <= n and j < len(ps) - 1:
        j += 1

    return ps[i-1:j];

def to_int(l):
    return int(''.join(map(str, l)))

cs = get_primes_between(1000,10000)

found = []

for c in cs:
    if len(str(c)) - len(set(str(c))) > 1:
        continue
    perms = itertools.permutations(str(c))
    perms = map(to_int, perms)
    perms = filter(lambda x: x in cs, perms)

    combos = itertools.combinations(perms, 3)
    for combo in combos:
        c = sorted(combo)
        if c[2] - c[1] == c[1] - c[0]:
            found.append(c)

print set(tuple(x) for x in found)
