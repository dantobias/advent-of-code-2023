def symbol(data, i, j):
    if i<0 or i >= len(data) or j<0 or j >= len(data[0]):
        return False
    elif (data[i][j] < '0' or data[i][j] > '9') and data[i][j] != '.' and data[i][j] != ' ' and data[i][j] != "\n":
        return True

def part_number_sum(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        total = 0
        for i in range(len(filedata)):
            currnum = ''
            adjsymbol = False
            for j in range(len(filedata[i])):
                if filedata[i][j] >= '0' and filedata[i][j] <= '9':
                    if not adjsymbol:
                        if symbol(filedata, i-1, j) or symbol(filedata, i+1, j) or symbol(filedata, i, j-1) or symbol(filedata, i, j+1) or symbol(filedata, i-1, j-1) or symbol(filedata, i-1, j+1) or symbol(filedata, i+1, j-1) or symbol(filedata, i+1, j+1):
                            adjsymbol = True                            
                    currnum += filedata[i][j]
                else:
                    if currnum and adjsymbol:
                        #print(currnum)
                        total += int(currnum)
                    currnum = ''
                    adjsymbol = False
    return total

print(part_number_sum('d03-p1-data.txt'))
