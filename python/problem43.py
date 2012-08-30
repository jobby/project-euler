ps = [2,3,5,7,11,13,17]

def to_int(l):
    return int(''.join(map(str, l)))

def is_special(n):
    if n[3] % 2 != 0: return False
    if n[5] != 0 and n[5] != 5: return False

    for x in range(7,0,-1):
        if to_int(n[x:x+3]) % ps[x-1] != 0:
            return False
    return True

def permute(a):
    k = -1
    for i in range(len(a) - 1, 0, -1):
        if a[i - 1] < a[i]:
            k = i - 1
            break

    if k == -1:
        return a

    for j in range(len(a) - 1, k, -1):
        if a[j] > a[k]:
            temp = a[j]
            a[j] = a[k]
            a[k] = temp
            break
    end = a[k+1:]
    end.reverse()
    return a[0:k+1] + end

x = ([0,1,2,3,4,5,6,7,8,9])

total = 0
while x != [9,8,7,6,5,4,3,2,1,0]:
    if is_special(x):
        total += to_int(x)
    x = permute(x)

print total
