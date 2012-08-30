def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def permute(a):
    k = -1
    for i in range(len(a) - 1, 0, -1):
        if a[i - 1] > a[i]:
            k = i - 1
            break

    if k == -1:
        return a

    for j in range(len(a) - 1, k, -1):
        if a[j] < a[k]:
            temp = a[j]
            a[j] = a[k]
            a[k] = temp
            break
    end = a[k+1:]
    end.reverse()
    return a[0:k+1] + end

def to_int(l):
    t = 0
    n = len(l)
    for i in range(0, n):
        t += l[i] * (10 ** (n - i - 1))
    return t

primes = get_primes(7654321)

x = [7,6,5,4,3,2,1]
while x != [1,2,3,4,5,6,7]:
    x = permute(x)
    if to_int(x) in primes:
        print "".join(map(str,x))
        break

