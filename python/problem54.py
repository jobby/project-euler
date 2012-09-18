def same_suit(cards):
    return len(set(map(lambda x: x[1], cards))) == 1

def score(cards):
    """
    Returns a tuple (a,b,c) where a is the rank (two pair, flush etc), b is the highest value card in the rank and c is the highest value card outside of the rank
    """
    
    values = sorted(map(lambda x: x[0], cards))

    if same_suit(cards) and values[0] == 10 and values[4] == 14: # royal flush
        return (10, 14, 0) 

    if same_suit(cards) and values[4] - values[0] == 4 and len(set(values)) == 5: # straigh flush
        return (9, values[4], 0)

    if len(set(values)) == 2 and values[1] == values[3]: # four of a kind
        if values[0] != values[1]:
            high_card = values[0]
        else: high_card = values[4]
        return (8, values[2], high_card)

    if len(set(values)) == 2 and values[1] != values[3]: # full house
        return (7, values[2], 0)

    if same_suit(cards): # flush
        return (6, values[4], 0)

    if values[4] - values[0] == 4 and len(set(values)) == 5: # straight
        return (5, values[4], 0)

    if len(set(values)) == 3: # three of a kind or two pair
        # three of a kind
        if values[0] == values[2]:
            return (4, values[0], max(values[3:5]))
        if values[1] == values[3]:
            return (4, values[1], max(values[0], values[4]))
        if values[2] == values[4]: 
            return (4, values[2], max(values[0:2]))
        else: # two pair
            return (3, max(values[1], values[3]), dict((values.count(i), i) for i in values)[1])

    if len(set(values)) == 4: # one pair
        high_value_card = dict((values.count(i), i) for i in values)[2]
        s = set(values)
        s.remove(high_value_card)
        return (2, high_value_card, max(s))

    return (1, values[4], 0)

def n(l):
    if l == 'T': return 10
    elif l == 'J': return 11
    elif l == 'Q': return 12
    elif l == 'K': return 13
    elif l == 'A': return 14
    else: return int(l)

def l2c(line):
    return map(lambda x: (n(x[0]), x[1]), line.rstrip().split(' '))

f = open("poker.txt")
lines = f.readlines()
f.close()

wins = 0
for line in lines:
    cards = l2c(line)
    p1_score = score(cards[0:5])
    p2_score = score(cards[5:])

    if p1_score > p2_score: wins += 1

print wins
