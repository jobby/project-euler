def is_pythagorean(x,y,z):
    return x ** 2 + y ** 2 == z ** 2

max = 999

for a in range(1, 998):
    for b in range(1, 999 - a):
        c = 1000 - a - b
        if is_pythagorean(a,b,c):
             print (a*b*c)
             break