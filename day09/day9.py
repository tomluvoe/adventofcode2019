#!/usr/bin/python3

import intcode

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def part1(data):
    ic = intcode.intcode(data,1,False)
    while ic.state_finish == False:
        #print('run')
        ic.run()
        ic.state()
        #print(ic.data)
    return ic.output

print("My data:\n", data, "\n")

print("** Part one")
print("My solution is: ", part1(data), "\n")
