def is_prime(x):
    if x == 2: return True
    for i in range(2,int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            return False
    return True

print filter(is_prime,range(2,1009999))[10000]