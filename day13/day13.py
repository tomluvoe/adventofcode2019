#!/usr/bin/python3

import intcode_refact

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def part1(data):
    count = 0
    ic = intcode_refact.intcode(data,state_wait=False)
    ic.run()
    for i in range(len(ic.output)//3):
        count += 1 if ic.output[i*3+2] == 2 else 0
    return count

def part2(data):
    data = '2'+data[1:]
    ic = intcode_refact.intcode(data,state_wait=True)
    ball = -1
    paddle = -1
    score = 0
    while True:
        ic.run()
        ic.run()
        ic.run()
        if ic.state_finish:
            break
        if ic.output[2] == 3:
            paddle = ic.output[0]
        if ic.output[2] == 4:
            ball = ic.output[0]
        if ic.output[0] == -1 and ic.output[1] == 0:
            score = ic.output[2]
        ic.output = []
        if ball >= 0 and paddle >= 0:
            ic.input = -1 if paddle > ball else 1 if ball > paddle else 0
    return score

print("My data:\n", data, "\n")

print("** Part one")
print("My solution is: ", part1(data), "\n")

print("** Part two")
print("My solution is: ", part2(data), "\n")
