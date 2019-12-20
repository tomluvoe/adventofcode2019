#!/usr/bin/python3

import intcode_refact

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def part1(data):
    white_panels = []
    black_panels = []
    directions_x = [-1,0,1,0]
    directions_y = [0,-1,0,1]
    dir = 1
    x = 0
    y = 0

    ic = intcode_refact.intcode(data,0,True)
    while True:
        ic.input = 1 if str(x)+':'+str(y) in white_panels else 0
        ic.run()
        ic.run()
        if ic.state_finish:
            break
        if ic.output[0]:
            white_panels.append(str(x)+':'+str(y))
        else:
            black_panels.append(str(x)+':'+str(y))
        dir = dir-1 if ic.output[1] == 0 else dir+1
        dir = dir % 4
        x += directions_x[dir]
        y += directions_y[dir]
        ic.output = []
    print(len(white_panels),len(black_panels))
    white_panels.extend(black_panels)
    print(len(white_panels))
    return len(list(set(white_panels)))

print("My data:\n", data, "\n")

print("** Part one")
print("My solution is: ", part1(data), "\n")

#print("** Part two")
#print("My solution is: ", part2(data), "\n")
