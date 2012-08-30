from bisect import bisect_left
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

limit = 1000000

ps = prime_sieve(limit)

def is_prime(ps, p): 
    i = bisect_left(ps, p)
    return i != len(ps) and ps[i] == p

seen = {}

longest_length = 1
longest_prime = 2

for i in range(0,len(ps) - 1):
    count = 0
    total = ps[i]
    while total < limit:
        count = count + 1
        total = total + ps[i + count]

        if count > 1 and count % 2 == 1:
            continue

        if count + 1 > longest_length and is_prime(ps, total):
            longest_length = count + 1
            longest_prime = total

print longest_prime
