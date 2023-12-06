def winnings(filename):
    total = 0
    with open(filename) as infile:
        filedata = infile.readlines()
        for line in filedata:
            score = 0
            [cardid, numbers] = line.rstrip().split(": ")
            [winning_numbers, your_numbers] = numbers.split(" | ")
            win_num = winning_numbers.split(" ")
            your_num = your_numbers.split(" ")
            for num in win_num:
                if num != '' and num in your_num:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
            total += score
    return total

print(winnings('d04-p1-data.txt'))
