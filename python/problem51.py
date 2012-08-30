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

def count_digits(n, digit):
    return len(filter(lambda x: int(x) == digit, str(n)))

def check_prime(p, digit_to_replace):
    total = 0
    for i in range(0,10):
        candidate = str(p).replace(str(digit_to_replace), str(i))
        if candidate[0] == '0': continue
        candidate = int(candidate)
        if is_prime(ps, candidate):
            total += 1
    return total
    

number_of_primes = 8

for change_digits in [1,3,5]:
    for p in ps:
        if p < 10 ** change_digits: continue

        found = False
        for i in range(0, 11 - number_of_primes):
            if count_digits(p, i) == change_digits:
                if check_prime(p, i) == number_of_primes:
                    print p
                    found = True
                    break
        if found:
            break
