#!/usr/bin/python3

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def fuel(m, r = False):
    if r:
        sum = 0
        x = m//3-2
        while x > 0:
            sum += x
            x = x//3-2
    else:
        sum = m//3-2
    return sum

def part1(data):
    mass = map(int, data.split('\n'))
    sum = 0
    for m in mass:
        sum += fuel(m)
    return sum

def part2(data):
    mass = map(int, data.split('\n'))
    sum = 0
    for m in mass:
        sum += fuel(m, True)
    return sum

def unit_test_p1():
    print("Unit test start:")
    assert fuel(12) == 2
    print("Test 1 OK")
    assert fuel(14) == 2
    print("Test 2 OK")
    assert fuel(1969) == 654
    print("Test 3 OK")
    assert fuel(100756) == 33583
    print("Test 4 OK")

def unit_test_p2():
    print("Unit test start:")
    assert fuel(14, True) == 2
    print("Test 1 OK")
    assert fuel(1969, True) == 966
    print("Test 2 OK")
    assert fuel(100756, True) == 50346
    print("Test 3 OK")

print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is: ", part2(data), "\n")
