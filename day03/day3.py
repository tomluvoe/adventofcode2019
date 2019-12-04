#!/usr/bin/python3

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1].split('\n')

def mv_tuple(cmd):
    t = (0,0)
    if cmd[0] == 'U':
        t = (0,1)
    elif cmd[0] == 'D':
        t = (0,-1)
    elif cmd[0] == 'L':
        t = (-1,0)
    else:
        t = (1,0)
    return t

def jp_tuple(cmd):
    t = (0,0)
    if cmd[0] == 'U':
        t = (0,int(cmd[1:]))
    elif cmd[0] == 'D':
        t = (0,-int(cmd[1:]))
    elif cmd[0] == 'L':
        t = (-int(cmd[1:]),0)
    else:
        t = (int(cmd[1:]),0)
    return t

def intersect(x0, dx, coord_list, cmd=False):
    dist = False
    if len(coord_list) > 1:
        for i in range(len(coord_list)-1):
            cx = sorted((coord_list[i][0],coord_list[i+1][0]))
            cy = sorted((coord_list[i][1],coord_list[i+1][1]))
            xx = sorted((x0[0],x0[0]+dx[0]))
            xy = sorted((x0[1],x0[1]+dx[1]))
            if dx[1] == 0:
                if xx[0] < cx[0] and xx[1] > cx[0] and cy[0] < xy[0] and cy[1] > xy[0]:
                    if dist == False or dist > sum(tuple(map(abs,(cx[0],xy[0])))):
                        dist = sum(tuple(map(abs,(cx[0],xy[0]))))
            else:
                if cx[0] < xx[0] and cx[1] > xx[0] and xy[0] < cy[0] and xy[1] > cy[0]:
                    if dist == False or dist > sum(tuple(map(abs,(xx[0],cy[0])))):
                        dist = sum(tuple(map(abs,(xx[0],cy[0]))))
    return dist

def intersect_p2(x0, dx, coord_list, cmd=False):
    dist = False
    if len(coord_list) > 1:
        for i in range(len(coord_list)-1):
            cx = sorted((coord_list[i][0],coord_list[i+1][0]))
            cy = sorted((coord_list[i][1],coord_list[i+1][1]))
            xx = sorted((x0[0],x0[0]+dx[0]))
            xy = sorted((x0[1],x0[1]+dx[1]))
            if dx[1] == 0:
                if xx[0] < cx[0] and xx[1] > cx[0] and cy[0] < xy[0] and cy[1] > xy[0]:
                    if dist == False or dist > sum(tuple(map(abs,(cx[0],xy[0])))):
                        dist = sum(tuple(map(abs,(cx[0],xy[0]))))
            else:
                if cx[0] < xx[0] and cx[1] > xx[0] and xy[0] < cy[0] and xy[1] > cy[0]:
                    if dist == False or dist > sum(tuple(map(abs,(xx[0],cy[0])))):
                        dist = sum(tuple(map(abs,(xx[0],cy[0]))))
    return dist

def part2(data): #add step to tuple for each item
    dist = False
    coord_list = []
    dist_list = []
    for line in data:
        x = (0,0)
        xl = [x]
        dl = [0]
        d = 0
        for s in line.split(','):
            #print(s)
            #print(coord_list)
            #print(dist_list)
            jmp = mv_tuple(s)
            for i in range(int(s[1:])): #loop distance
                d += 1
                x = tuple(map(sum,zip(x,jmp)))
                #print(x)
                if x in coord_list:
                    i = coord_list.index(x)
                    if dist == False or dist > dist_list[i] + d:
                        dist = d + dist_list[i]
                xl.append(x)
                dl.append(d)
        coord_list.extend(xl)
        dist_list.extend(dl)
    #print (dist)
    return dist

def part1(data):
    dist = False
    coord_list = []
    for line in data:
        x = (0,0)
        xl = [x]
        for s in line.split(','):
            jmp = jp_tuple(s)
            x0 = x
            x = tuple(map(sum,zip(x,jmp)))
            a = intersect(x0,jmp,coord_list,s)
            if a != False and (dist == False or a < dist):
                dist = a
            xl.append(x)
        coord_list.extend(xl)
    return dist

def unit_test_p1():
    print("Unit test start:")
    assert part1(['R8,U5,L5,D3','U7,R6,D4,L4']) == 6
    print("Test 1 OK")
    assert part1(['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']) == 159
    print("Test 2 OK")
    assert part1(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']) == 135
    print("Test 3 OK")

def unit_test_p2():
    print("Unit test start:")
    assert part2(['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']) == 610
    print("Test 1 OK")
    assert part2(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']) == 410
    print("Test 2 OK")

print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is: ", part2(data), "\n")
