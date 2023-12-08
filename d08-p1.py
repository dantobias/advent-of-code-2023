import re

def do_moves(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        moves = None
        nodes = {}
        for line in filedata:
            line = line.rstrip()
            if line != "":
                if moves == None:
                    moves = line
                    #print(moves)
                else:
                    (node, paths) = line.split(" = ")
                    paths = paths.replace('(', '')
                    paths = paths.replace(')', '')
                    (left, right) = paths.split(', ')
                    #print(node, left, right)
                    nodes[node] = (left, right)

    #print(nodes)
        
    steps = 0
    currnode = 'AAA'
    currmove = 0
    while True:
        steps += 1
        if moves[currmove] == 'L':
            currnode = nodes[currnode][0]
        elif moves[currmove] == 'R':
            currnode = nodes[currnode][1]

        #print(steps, currnode, currmove, moves[currmove])

        if currnode == 'ZZZ':
            return steps
        elif currmove < len(moves)-1:
            currmove += 1
        else:
            currmove = 0

print(do_moves('d08-p1-data.txt'))
