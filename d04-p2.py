def winnings(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        numcards = len(filedata)*[1]
        cardno = 0
        for line in filedata:
            cardno += 1
            score = 0
            [cardid, numbers] = line.rstrip().split(": ")
            [winning_numbers, your_numbers] = numbers.split(" | ")
            win_num = winning_numbers.split(" ")
            your_num = your_numbers.split(" ")
            for num in win_num:
                if num != '' and num in your_num:
                    score += 1
            for i in range(cardno, cardno+score):
                numcards[i] += numcards[cardno-1]

    total = 0
    for n in numcards:
        total += n
    return total

print(winnings('d04-p1-data.txt'))
