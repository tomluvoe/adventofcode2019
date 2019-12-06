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

def map_to_node(node,target,objects,map):
    found = False
    if target in map:
        return map, True
    if node in objects.keys():
        for o in range(len(objects[node])):
            map.append(objects[node][o])
            map, found = map_to_node(objects[node][o],target,objects,map)
            if found:
                return map, found
    if not found:
        map = map[:-1]
    return map, found

def create_map(data):
    objects = dict()
    for obs in data.split('\n'):
        o = obs.split(')')
        if o[0] in objects:
            objects[o[0]].extend([o[1]])
            pass
        else:
            objects[o[0]] = [o[1]]
    return objects

def count_unique(data,ignore):
    unique = []
    removed = []
    count = 0
    for d in data:
        if d in ignore:
            continue
        if d in unique:
            if d not in removed:
                count -= 1
                removed.append(d)
        else:
            unique.append(d)
            count += 1
    return count

def part1(data):
    return c_rec('COM',create_map(data))

def part2(data):
    objects = create_map(data)
    san, b = map_to_node('COM','SAN',objects,[])
    you, b = map_to_node('COM','YOU',objects,[])
    san.extend(you)
    return count_unique(san,['SAN','YOU'])

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

def unit_test_p2():
    print("Unit test start:")
    assert part2(
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
K)L
K)YOU
I)SAN""") == 4
    print("Test 1 OK")

print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is: ", part2(data), "\n")
