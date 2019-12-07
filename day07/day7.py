#!/usr/bin/python3

import intcode
import itertools

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def part1(data, input=0):
    max_thrust = 0
    for phase in list(itertools.permutations([0,1,2,3,4])):
        thrust = intcode.thrusters(data,phase)
        if thrust > max_thrust:
            max_thrust = thrust
    return max_thrust

print("My data:\n", data, "\n")

print("** Part one")
print("My solution is: ", part1(data), "\n")
