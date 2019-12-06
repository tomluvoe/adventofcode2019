#!/usr/bin/python3

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def c_rec(node,objects,depth=1):
    orbits = 0
    if node in objects.keys():
        for o in range(len(objects[node])):
            orbits += c_rec(objects[node][o],objects,depth+1)
            orbits += depth
    return orbits

def part1(data):
    objects = dict()
    for obs in data.split('\n'):
        o = obs.split(')')
        if o[0] in objects:
            objects[o[0]].extend([o[1]])
            pass
        else:
            objects[o[0]] = [o[1]]
    return c_rec('COM',objects)

def unit_test_p1():
    print("Unit test start:")
    assert part1(
"""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""") == 42
    print("Test 1 OK")


print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(data), "\n")
