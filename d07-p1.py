import re

def card_rank(card):
    if card >= '2' and card <= '9':
        return int(card)
    elif (card == 'T'):
        return(10)
    elif (card == 'J'):
        return(11)
    elif (card == 'Q'):
        return(12)
    elif (card == 'K'):
        return(13)
    elif (card == 'A'):
        return(14)
    else:
        return(0)

def hand_rank(hand):
    cardvals = []
    cardcounts = []
    for c in hand[0]:
        found = False
        for i in range(len(cardvals)):
            if cardvals[i] == c:
                found = True
                cardcounts[i] += 1
        if not found:
            cardvals.append(c)
            cardcounts.append(1)

    #print (cardvals, cardcounts)

    maxcount = 0
    twocount = 0
    for i in range(len(cardvals)):
        if cardcounts[i] > maxcount:
            maxcount = cardcounts[i]
        if cardcounts[i] == 2:
            twocount += 1

    rankval = 0
    if maxcount == 5: # 5 of a kind
        rankval = 70000000000
    elif maxcount == 4: # 4 of a kind
        rankval = 60000000000
    elif maxcount == 3 and twocount == 1: # full house
        rankval = 50000000000
    elif maxcount == 3: # 3 of a kind
        rankval = 40000000000
    elif maxcount == 2 and twocount == 2: # 2 pair
        rankval = 30000000000
    elif maxcount == 2: # pair
        rankval = 20000000000
    else:
        rankval = 10000000000

    valadd = 0
    for c in hand[0]:
        valadd *= 100
        valadd += card_rank(c)

    rankval += valadd

    return rankval

def winnings(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        hands = []
        for line in filedata:
            line = line.rstrip()
            if line != "":
                (cards, bid) = line.split(" ")
            hands.append((cards, int(bid)))
    hands.sort(key=hand_rank)

    result = 0
    for i in range(len(hands)):
        #print(hands[i])
        result += (i + 1) * hands[i][1]        

    return result

print(winnings('d07-p1-data.txt'))
