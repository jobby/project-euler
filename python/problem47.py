
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

ps = prime_sieve(1000000)

def get_primes_upto(n):
    i = 0
    while ps[i] <= n:
        i += 1
    return ps[0:i+1];

def trial_division(n):
    if n == 1: return [1]
    primes = get_primes_upto(int(n**0.5) + 1)
    prime_factors = []
 
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1: prime_factors.append(n)
 
    return prime_factors

def unique_factors(n):
    return len(set(trial_division(n)))

fs = [0]
c = 0
for i in range(1,1000000):
    c+= 1
    fs.append(unique_factors(i))
    if len(fs) > 4:
        if fs[-4:] == [4,4,4,4]:
            print c -3
            break

