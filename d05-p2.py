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
                    ranges = []
                    for i in range(0, len(values), 2):
                        ranges.append((values[i], values[i+1]))
                    newranges = ranges.copy()
                elif tempitems[1] == "map:":
                    #print(currmap, newranges)
                    currmap = tempitems[0]
                    ranges = newranges
                    newranges = ranges.copy()
                else:
                    (mapdest, mapsource, maplen) = line.split(" ")
                    mapdest = int(mapdest)
                    mapsource = int(mapsource)
                    maplen = int(maplen)
                    mapstart = mapsource
                    mapend = mapsource + maplen # actually 1 past end
                    mapdiff = mapdest - mapsource
                    for i in range(len(ranges)):
                        (start, size) = ranges[i]
                        end = start + size 
                        if (mapstart <= start) and (mapend >= end): # entire range is within map item
                            newranges[i] = (start + mapdiff, size)
                            #print("A", i, newranges[i])
                        elif (mapstart > start) and (mapstart < end) and (mapend >= end): # range starts in middle of map item and map extends to end of it
                            newranges[i] = (start, mapstart - start) # unchanged part
                            ranges[i] = (start, mapstart - start) # unchanged part
                            newranges.append((mapdest, end - mapstart)) # add new item for changed part
                            #print("B", i, newranges[i], (mapdest, end - mapstart))
                        elif (mapstart <= start) and (mapend > start) and (mapend < end): # range ends in middle of map item
                            newranges[i] = (mapend, end - mapend) # unchanged part
                            ranges[i] = (mapend, end - mapend) # unchanged part
                            newranges.append((start + mapdiff, mapend - start)) # changed part
                            #print("C", i, newranges[i], (start + mapdiff, mapend - start))
                        elif (mapstart > start) and (mapend < end): # range is entirely within map item
                            newranges[i] = (start, mapstart - start) # first unchanged part
                            ranges[i] = (start, mapstart - start) # first unchanged part
                            newranges.append((mapend, end - mapend)) # second unchanged part
                            ranges.append((mapend, end - mapend)) # second unchanged part
                            newranges.append((mapdest, maplen)) # changed part
                            #print("D", i, newranges[i], (mapend, end - mapend), (mapdest, maplen))
    minval = None
    for v in newranges:
        if minval == None or v[0] < minval:
            minval = v[0]
    return minval

print(find_location('d05-p1-data.txt'))
