def it(n):
    if (n % 2 == 0): 
       return n / 2
    else:
	return 3 * n + 1

# manual memoization
cache = {}
def seq_length(x):
    if x == 1: return 1
    else: 
        if x in cache:
            return cache[x]
        else:
            res = 1 + seq_length(it(x))
            cache[x] = res
            return res

max_chain_length = 0
biggest = 0

for i in range(1,1000000):
    l = seq_length(i)
    if l > max_chain_length: 
        max_chain_length = l
        biggest = i

print biggest

