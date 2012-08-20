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

x = [0,1,2,3,4,5,6,7,8,9]
for i in range(0,999999):
    x = permute(x)

print x
    
