def find_calibration_value(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        total = 0
        for line in filedata:
            firstdigit = ''
            lastdigit = ''
            for p in range(len(line)):
                digit = ''
                if line[p] >= '0' and line[p] <= '9':
                    digit = line[p]
                elif line[p:p+3] == 'one':
                    digit = '1'
                elif line[p:p+3] == 'two':
                    digit = '2'
                elif line[p:p+5] == 'three':
                    digit = '3'
                elif line[p:p+4] == 'four':
                    digit = '4'
                elif line[p:p+4] == 'five':
                    digit = '5'
                elif line[p:p+3] == 'six':
                    digit = '6'
                elif line[p:p+5] == 'seven':
                    digit = '7'
                elif line[p:p+5] == 'eight':
                    digit = '8'
                elif line[p:p+4] == 'nine':
                    digit = '9'

                if digit != '':
                    if firstdigit == '':
                        firstdigit = digit
                    lastdigit = digit

            #print(firstdigit+lastdigit)
            total += int(firstdigit+lastdigit)
    return total

print(find_calibration_value('d01-p1-data.txt'))
