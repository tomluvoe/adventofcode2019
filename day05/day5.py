#!/usr/bin/python3

import itertools

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def step(dat,pc=0,input=0):
    cmd = ['','+','*','storeinputataddr','outputaddr']
    instr = int(dat[pc])
    pm = '00'
    p1 = 0
    p2 = 0
    if len(str(instr)) > 2:
        instr = int(str(dat[pc])[-2:])
        pm = '00'+str(dat[pc])[:-2]
    if pm[-1] == '0':
        p1 = dat[dat[pc+1]]
    else:
        p1 = dat[pc+1]
    if instr < 3 or instr > 4:
        if pm[-2] == '0':
            p2 = dat[dat[pc+2]]
        else:
            p2 = dat[pc+2]
    if(instr < 3):
        dat[dat[pc+3]] = eval(str(p1)+cmd[instr]+str(p2))
        pc += 4
    elif(instr == 3):
        dat[dat[pc+1]] = input
        pc += 2
    elif(instr == 4):
        print(p1)
        pc += 2
    elif(instr == 5):
        if p1 == 0:
            pc += 3
        else:
            pc = p2
    elif(instr == 6):
        if p1 == 0:
            pc = p2
        else:
            pc += 3
    elif(instr == 7):
        if p1 < p2:
            dat[dat[pc+3]] = 1
        else:
            dat[dat[pc+3]] = 0
        pc += 4
    elif(instr == 8):
        if p1 == p2:
            dat[dat[pc+3]] = 1
        else:
            dat[dat[pc+3]] = 0
        pc += 4
    return dat,pc

def part1(data, input=0):
    dat = list(map(int, data.split(',')))
    pc = 0
    while dat[pc] != 99:
        dat,pc = step(dat,pc,input)
    return dat

def unit_test_p1():
    print("Unit test start:")
    assert part1("1002,4,3,4,33") == [1002,4,3,4,99]
    print("Test 1 OK")
    assert part1("1101,100,-1,4,0") == [1101,100,-1,4,99]
    print("Test 2 OK")

def unit_test_p2():
    print("Unit test start;")
    dat = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    assert part1(dat,1)[0]
    print("Test 1 OK if 999 output")
    assert part1(dat,8)[0]
    print("Test 2 OK if 1000 output")
    assert part1(dat,9)[0]
    print("Test 3 OK if 1001 output")

print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
part1(data,1)

print("** Part two")
unit_test_p2()
part1(data,5)
