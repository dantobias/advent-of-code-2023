def find_location(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        currmap = None
        values = []
        for line in filedata:
            line = line.rstrip()
            if line != "":
                tempitems = line.split(" ")
                if tempitems[0] == "seeds:":
                    (dummy, seedvals) = line.split(": ")
                    values = seedvals.split(" ")
                    values = [int(x) for x in values]
                    newvalues = values.copy()
                elif tempitems[1] == "map:":
                    #print(currmap, newvalues)
                    currmap = tempitems[0]
                    values = newvalues
                    newvalues = values.copy()
                else:
                    (mapdest, mapsource, maplen) = line.split(" ")
                    mapdest = int(mapdest)
                    mapsource = int(mapsource)
                    maplen = int(maplen)
                    for i in range(len(values)):
                        if values[i] >= mapsource and values[i] < mapsource + maplen:
                            newvalues[i] = mapdest + (values[i] - mapsource)
                    #print(mapdest, mapsource, maplen, newvalues)
    minval = None
    for v in newvalues:
        if minval == None or v < minval:
            minval = v
    return minval

print(find_location('d05-p1-data.txt'))
