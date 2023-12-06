def possible_games(filename, bagred, baggreen, bagblue):
    with open(filename) as infile:
        filedata = infile.readlines()
        total = 0
        for line in filedata:
            gameok = True
            [game, data] = line.rstrip().split(": ")
            [dummy, gameno] = game.split(" ")
            gameno = int(gameno)
            sets = data.split("; ")
            for s in sets:
                red = 0
                green = 0
                blue = 0
                balls = s.split(", ")
                for b in balls:
                    [num, color] = b.split(" ")
                    num = int(num)
                    if color == "red":
                        red += num
                    elif color == "green":
                        green += num
                    elif color == "blue":
                        blue += num
                if red > bagred or green > baggreen or blue > bagblue:
                    gameok = False
            if gameok:
                #print(gameno)
                total += gameno
    return total

print(possible_games('d02-p1-data.txt', 12, 13, 14))
