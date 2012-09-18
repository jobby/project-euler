def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    for i in range(1, 51):
        n = n + int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True

print len(filter(is_lychrel, range(1,10000)))
