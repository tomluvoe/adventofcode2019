#!/usr/bin/python3

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.readlines()

def fuel(mass):
    return int(mass)//3-2

def fuel_r(mass):
    if fuel(mass) > 0:
        return fuel(mass) + fuel_r(fuel(mass))
    return 0

def fuel_sum(mass):
    sum = 0
    for i in range(len(mass)):
        sum += fuel(mass[i])
    return sum

def fuel_sum_r(mass):
    sum = 0
    for i in range(len(mass)):
        sum += fuel_r(mass[i])
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
    assert fuel_r(14) == 2
    print("Test 1 OK")
    assert fuel_r(1969) == 966
    print("Test 2 OK")
    assert fuel_r(100756) == 50346
    print("Test 3 OK")

print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", fuel_sum(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is: ", fuel_sum_r(data), "\n")
