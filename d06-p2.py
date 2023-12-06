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
                    racetime = ""
                    for item in items[1:]:
                        racetime += item
                    racetime = int(racetime)
                elif items[0] == 'Distance:':
                    racedist = ""
                    for item in items[1:]:
                        racedist += item
                    racedist = int(racedist)
    #print(racetime, racedist)
    result = 0
    for t in range(racetime+1):
        dist = (racetime - t) * t
        if dist > racedist:
            result += 1
    return result

print(num_records('d06-p1-data.txt'))
