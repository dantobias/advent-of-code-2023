def issymbol(data, i, j):
    if i<0 or i >= len(data) or j<0 or j >= len(data[0]):
        return False
    elif (data[i][j] < '0' or data[i][j] > '9') and data[i][j] != '.' and data[i][j] != ' ' and data[i][j] != "\n":
        return True

def isnumber(data, i, j):
    if i<0 or i >= len(data) or j<0 or j >= len(data[0]):
        return False
    elif (data[i][j] >= '0' and data[i][j] <= '9'):
        return True

def getgearstatus(data, i, j):
    if i<0 or i >= len(data) or j<0 or j >= len(data[0]):
        return 0
    else:
        return data[i][j]

def gear_sum(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        gearstatus = []
        for i in range(len(filedata)):
            gearstatus.append([])
            for j in range(len(filedata[i])):
                partcount = 0
                if issymbol(filedata, i, j):
                    if isnumber(filedata, i-1, j-1):
                        partcount += 1
                    if isnumber(filedata, i-1, j) and not isnumber(filedata, i-1, j-1):
                        partcount += 1
                    if isnumber(filedata, i-1, j+1) and not isnumber(filedata, i-1, j):
                        partcount += 1
                    if isnumber(filedata, i, j-1):
                        partcount += 1
                    if isnumber(filedata, i, j+1):
                        partcount += 1
                    if isnumber(filedata, i+1, j-1):
                        partcount += 1
                    if isnumber(filedata, i+1, j) and not isnumber(filedata, i+1, j-1):
                        partcount += 1
                    if isnumber(filedata, i+1, j+1) and not isnumber(filedata, i+1, j):
                        partcount += 1

                    if partcount == 2:
                        #print(i, j)
                        #print(gearstatus)
                        gearstatus[i].append(1)
                    else:
                        gearstatus[i].append(0)
                else:
                    gearstatus[i].append(0)

        for i in range(len(filedata)):
            currnum = ''
            gears = set()
            for j in range(len(filedata[i])):
                if isnumber(filedata, i, j):
                    if getgearstatus(gearstatus, i-1, j-1):
                        gears.add((i-1, j-1))
                    if getgearstatus(gearstatus, i-1, j):
                        gears.add((i-1, j))
                    if getgearstatus(gearstatus, i-1, j+1):
                        gears.add((i-1, j+1))
                    if getgearstatus(gearstatus, i, j-1):
                        gears.add((i, j-1))
                    if getgearstatus(gearstatus, i, j+1):
                        gears.add((i, j+1))
                    if getgearstatus(gearstatus, i+1, j-1):
                        gears.add((i+1, j-1))
                    if getgearstatus(gearstatus, i+1, j):
                        gears.add((i+1, j))
                    if getgearstatus(gearstatus, i+1, j+1):
                        gears.add((i+1, j+1))

                    currnum += filedata[i][j]
                else:
                    if gears:
                        #print(currnum, gears)
                        for g in gears:
                            gearstatus[g[0]][g[1]] *= int(currnum)
                    currnum = ''
                    gears = set()

        total = 0
        for i in range(len(filedata)):
            for j in range(len(filedata[i])):
                total += gearstatus[i][j]
    return total

print(gear_sum('d03-p1-data.txt'))
