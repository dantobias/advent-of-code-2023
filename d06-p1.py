import re

def num_records(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        racetime = []
        racedist = []
        for line in filedata:
            line = line.rstrip()
            if line != "":
                items = re.split(r" +", line)
                #print(items)
                if items[0] == 'Time:':
                    racetime = items[1:]
                    racetime = [int(x) for x in racetime]
                elif items[0] == 'Distance:':
                    racedist = items[1:]
                    racedist = [int(x) for x in racedist]
    #print(racetime, racedist)
    result = 1
    for i in range(len(racetime)):
        raceresult = 0
        for t in range(racetime[i]+1):
            dist = (racetime[i] - t) * t
            #print(i, t, dist)
            if dist > racedist[i]:
                raceresult += 1
        result *= raceresult
        #print(i, raceresult, result)
    return result

print(num_records('d06-p1-data.txt'))
