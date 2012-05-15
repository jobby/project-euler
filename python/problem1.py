# Obvious
total = 0
for i in range(1,1000):
    if (i % 3 == 0 or i % 5 == 0):
        total = total +  i
print total

# Hurray for list functions
def fizzbuzz(x): return x % 3 == 0 or x % 5 == 0
print sum(filter(fizzbuzz,range(1,1000)))

# One line
print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1,1000)))