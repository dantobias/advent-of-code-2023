import re

def do_moves(filename):
    with open(filename) as infile:
        filedata = infile.readlines()
        moves = None
        nodes = {}
        currnodes = []
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

                    if node[-1] == 'A':
                        currnodes.append(node)

    #print(nodes)

    # When running the steps straightforwardly, it takes too many steps to ever reach
    # the 'all ending in Z' state. But it was observed that all states with at least
    # one Z seem to come at the move at the end of the list of moves, so let's
    # make a table of where each node leads after that set of 271 steps.

    endnode = {}

    for n in nodes:
        currnode = n
        for m in moves:
            if m == 'L':
                currnode = nodes[currnode][0]
            elif m == 'R':
                currnode = nodes[currnode][1]
        endnode[n] = currnode


    # Even going 271 steps at a time it's too slow to make it to a solution. Let's see
    # if there's a pattern to each individual starting node reaching "Z" nodes.
    # As it turns out, they all repeat themselves, reaching a "Z" node in the same number
    # of repetitions of 271 steps, each a prime number, so they will all coincide, giving
    # an occurrence of all six being a "Z" node at the multiple of these numbers of
    # repetitions, times 271.

    result = 271
    for n in currnodes:
        currnode = n
        steps = 0
        prevsteps = 0
        count = 0
        while count<1: # I used a larger number at first to see the pattern
            steps += 271
            currnode = endnode[currnode]    
            if currnode[-1] == 'Z':
                stepcount = (steps-prevsteps)/271
                #print(n, steps, currnode, stepcount)
                prevsteps = steps
                count += 1
        result *= stepcount

    return int(result)

print(do_moves('d08-p1-data.txt'))
