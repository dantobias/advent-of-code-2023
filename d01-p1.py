def find_calibration_value(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        total = 0
        for line in filedata:
            firstdigit = ''
            lastdigit = ''
            for c in line:
                if c >= '0' and c <= '9':
                    if firstdigit == '':
                        firstdigit = c
                    lastdigit = c
            #print(firstdigit+lastdigit)
            total += int(firstdigit+lastdigit)
    return total

print(find_calibration_value('d01-p1-data.txt'))
