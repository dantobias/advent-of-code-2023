def game_power(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        total = 0
        for line in filedata:
            gameok = True
            [game, data] = line.rstrip().split(": ")
            [dummy, gameno] = game.split(" ")
            gameno = int(gameno)
            minred = 0
            mingreen = 0
            minblue = 0
            sets = data.split("; ")
            for s in sets:
                red = 0
                green = 0
                blue = 0
                balls = s.split(", ")
                for b in balls:
                    #print(b)
                    [num, color] = b.split(" ")
                    num = int(num)
                    if color == "red":
                        red += num
                    elif color == "green":
                        green += num
                    elif color == "blue":
                        blue += num
                #print('*', red, green, blue)
                if red > minred:
                    minred = red
                if green > mingreen:
                    mingreen = green
                if blue > minblue:
                    minblue = blue
            power = minred * mingreen * minblue
            #print(gameno, minred, mingreen, minblue, power)
            total += power
    return total

print(game_power('d02-p1-data.txt'))
