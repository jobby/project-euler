from operator import xor

# range(97, 124)

f = open('cipher1.txt')
e = f.read()
f.close()

e = map(int, e.split(','))

start = ord('a')
finish = ord('z') + 1

for key in [[a,b,c] for a in range(start, finish) for b in range(start, finish) for c in range(start, finish)]:
    d = ''
    for i in range(0, len(e), 3):
        d += chr(xor(e[i], key[0]))
        if i + 1 < len(e): d += chr(xor(e[i + 1], key[1]))
        if i + 2 < len(e): d += chr(xor(e[i + 2], key[2]))

    if d.find(' the ') != -1:
        print sum(map(ord, d))
        break



