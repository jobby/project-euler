limit = 20

divisor = 1
for i in range(1, limit + 1):
    step = divisor
    while(divisor % i != 0):
        divisor += step

print divisor