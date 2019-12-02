#!/usr/bin/python3

import itertools

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def step(dat,pc=0):
    cmd = ['','+','*']
    dat[dat[pc+3]] = eval(str(dat[dat[pc+1]])+cmd[dat[pc]]+str(dat[dat[pc+2]]))
    return dat

def part1(data, part1=0):
    dat = list(map(int, data.split(',')))
    pc = 0
    if part1:
        dat[1] = 12
        dat[2] = 2
    while dat[pc] != 99:
        dat = step(dat,pc)
        pc += 4
    return dat

def part2(data, output=19690720):
    for noun, verb in list(itertools.product(range(0,100),range(0,100))):
        dat = list(map(int, data.split(',')))
        pc = 0
        dat[1] = noun
        dat[2] = verb
        while dat[pc] != 99:
            dat = step(dat,pc)
            pc += 4
        if dat[0] == output:
            break
    return noun, verb

def unit_test_p1():
    print("Unit test start:")
    assert part1("1,0,0,0,99") == [2,0,0,0,99]
    print("Test 1 OK")
    assert part1("2,3,0,3,99") == [2,3,0,6,99]
    print("Test 2 OK")
    assert part1("2,4,4,5,99,0") == [2,4,4,5,99,9801]
    print("Test 3 OK")
    assert part1("1,1,1,4,99,5,6,0,99") == [30,1,1,4,2,5,6,0,99]
    print("Test 4 OK")
    assert part1("1,9,10,3,2,3,11,0,99,30,40,50") == [3500,9,10,70,2,3,11,0,99,30,40,50]
    print("Test 5 OK")


print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(data,1)[0], "\n")

print("** Part two")
print("My solution is:", part2(data), "\n")
