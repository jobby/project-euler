import math

tris = map(lambda n: n * (n + 1) * 1/2, range(1,21))

def is_triangle_word(w):
    s = sum(map(lambda l: ord(l) - 64, w))
    return s in tris

f = open("words.txt")
s = f.read()
f.close()

words = map(lambda x: x[1:-1], s.split(','))
print len(filter(is_triangle_word, words))
