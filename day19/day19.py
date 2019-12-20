#!/usr/bin/python3

import intcode_refact
import math

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def part1(data):
    count = 0
    for y in range(0,50):
        for x in range(0,50):
            ic = intcode_refact.intcode(data,[x,y],state_wait=False)
            ic.run()
            print(ic.output[0],end='')
            count += ic.output[0]
        print()
    return count


def part2(data):
    y00 = 1000
    x00 = -1
    x11 = -1

    for x in range(100,1000):
        ic = intcode_refact.intcode(data,[x,y00],state_wait=False)
        ic.run()
        print(ic.output[0],end='')
        if ic.output[0] == 1 and x00 == -1:
            x00 = x
        if ic.output[0] == 0 and (x00 != -1 and x11 == -1):
            x11 = x-1
    print()
    print('\n',x00,x11)
    delta_a1 = x00/y00
    delta_a2 = x11/y00
    print('angle line 1:',math.atan(delta_a1))
    print('angle line 2:',math.atan(delta_a2))

    approx_y = 0
    approx_x0 = 0
    approx_x1 = 0

    for y in range(1050,1100):
        y0 = y
        y1 = y + 99
        x1 = delta_a1 * y1
        x0 = delta_a2 * y0
        print('coord a1:',x1,y1,'coord a2:',x0,y0,'distance x:',x0-x1)
        if round(x0 - x1) >= 99:
            approx_y = y -10
            approx_x0 = int(delta_a1 * y0) - 5
            approx_x1 = int(delta_a2 * y1) + 5
            break

    print(approx_y, approx_x0, approx_x1)

    output = []
    for y in range(approx_y,approx_y+110):
        x0 = -1
        x1 = -1
        line = []
        for x in range(approx_x0,approx_x1):
            ic = intcode_refact.intcode(data,[x,y],state_wait=False)
            ic.run()
            #print(ic.output[0],end='')
            line.append(ic.output[0])
            if ic.output[0] == 1 and x0 == -1:
                x0 = x
            if ic.output[0] == 0 and (x0 != -1 and x1 == -1):
                x1 = x-1
        print([x0,x1,y])
        output.append([x0,x1,y])

    for i in range(len(output)-99):
        print('Evaluate output',i,output[i],output[i+99],output[i][1] - output[i+99][0])
        #if output[i][1] - output[i][0] and output[i+100][0] == 1:
        if output[i][1] - output[i+99][0] >= 99:
            resultx = output[i+99][0]
            resulty = output[i][2]
            break

    return resultx*10000+resulty

#    x0-x1 == 100
#    x11/y00 * y0 - x00/y00 * y1 = 100
#    x11/y00 * y - x00/y00 * (y+100) = 100

#    for y in range(1000,1001):
#        y0 = y
#        y1 = y + 100
#        x1 = x00/y00 * y1
#        x0 = x11/y00 * y0
#        print('angle1:',x1,y1,'angle2:',x0,y0,'diff x',x0-x1)
    #....p1
    #p0....
    # ==> x0 == x1
    # ==> y1 - y0 = 100
    # x0/y = tan (angle)
    # y0 = y, y1 = y+100
    # x0 = angle1,y1, x1=angle2,y0
    #(math.tan()-math.tan()) * x = 150
    # ((x1-x0)/1000) * x = 150
    # ((x1-x0)/1000) * x = 150 / ((x1-x0)/1000)


print("My data:\n", data, "\n")

print("** Part one")
#print("My solution is: ", part1(data), "\n")

print("** Part two")
print("My solution is: ", part2(data), "\n")
