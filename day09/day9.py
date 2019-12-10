#!/usr/bin/python3

import intcode

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def part1(data):
    ic = intcode.intcode(data,1,False)
    ic.run()
    return ic.output[0]

def part2(data):
    ic = intcode.intcode(data,2,False)
    ic.run()
    return ic.output[0]

print("My data:\n", data, "\n")

print("** Part one")
print("My solution is: ", part1(data), "\n")

print("** Part two")
print("My solution is: ", part2(data), "\n")
