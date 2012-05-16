def isPalindrome(x):
    return str(x)[::-1] == str(x)

biggest = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if isPalindrome(i * j) and i * j > biggest:
            biggest = i * j

print biggest