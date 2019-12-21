#!/usr/bin/python3

import math

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def visible_asteroids(pos,data):
    ast = []
    ast_pos = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if [x,y] != pos:
                if data[y][x] == '#':
                    dy = y-pos[1]
                    dx = x-pos[0]
                    ast.append(math.atan2(dy,dx))
                    ast_pos.append([math.atan2(dy,dx),math.sqrt(dx*dx+dy*dy),x,y])
    return ast,ast_pos

def best_position(data):
    max_asteroids = 0
    best_pos = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                a,ap = visible_asteroids([x,y],data)
                a = len(list(set(a)))
                if max_asteroids < a:
                    max_asteroids = a
                    best_pos = [x,y]
    return max_asteroids,best_pos

def find_200th(data,pos):
    ast,asteroids = visible_asteroids(pos,data)
    #print('ASTEROIDS pos',pos,'asteroids',asteroids)
    for i in range(len(asteroids)):
        asteroids[i][0] = (asteroids[i][0]+math.pi/2)
        asteroids[i][0] = asteroids[i][0] if asteroids[i][0] >= 0 else asteroids[i][0] + 2*math.pi
    asteroids.sort(key=lambda x:x[1])
    asteroids.sort(key=lambda x:x[0])
    print(asteroids)
    angle = -1
    i = 0
    xy = []
    found = 0
    #print(asteroids[0],asteroids[i][0] <= angle)
    while True:
        #print('loop',i,asteroids[i][0] <= angle)
        brk = 0
        while asteroids[i][0] <= angle:
            i += 1
            if i >= len(asteroids):
                i = 0
                angle = -1
            print('step',asteroids[i])
        found += 1
        angle = asteroids[i][0]
        print('asteroid destroyed:',found,i,asteroids[i])
        asteroids[i][0] = -100
        #i += 1
        if found == 200:
            xy = asteroids[i][2:4]
        if found >= len(asteroids):
            break
    return xy

def part1(data):
    data = data.split('\n')
    return best_position(data)[0]

def part2(data):
    print(data)
    data = data.split('\n')
    no,pos = best_position(data)
    print('best position',pos)
    pos = find_200th(data,pos)
    print(pos)
    return pos[0]*100+pos[1]

def test_day10_p1():
    print("Unit test start day10 p1:")
    test_data = """.#..#
.....
#####
....#
...##"""
    assert part1(test_data) == 8
    print("Test 1 OK")
    test_data = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""
    assert part1(test_data) == 33
    print("Test 2 OK")
    test_data = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""
    assert part1(test_data) == 35
    print("Test 3 OK")
    test_data =""".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""
    assert part1(test_data) == 41
    print("Test 4 OK")
    test_data = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""
    assert part1(test_data) == 210
    print("Test 5 OK")

def test_day10_p2():
    print("Unit test start day10 p2:")
    test_data = """..#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""
    #assert part2(test_data) == 802
    part2(test_data) == 802
    print("Test 1 OK")

print("My data:\n", data, "\n")

print("** Part one")
test_day10_p1()
print("My solution is: ", part1(data), "\n")

print("** Part two")
test_day10_p2()
print("My solution is: ", part2(data), "\n")
