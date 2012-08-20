def score(s):
    return sum(map(lambda x: ord(x) - 64, s))

f = open('names.txt')
lines = f.read()
f.close()

names = lines[1:-1].split("\",\"")
names.sort()

# print sum(map(lambda t: t[0] * t[1], zip(range(1,len(names) + 1), map(score, names))))

i = 1
total = 0
for name in names:
    total = total + i * score(name)
    i = i + 1

print total

