#!/usr/bin/python3

import intcode_refact
#import random

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def part1(data):
    ic = intcode_refact.intcode(data)
    pos = [20,20]
    #mymap = [[-1]*20]*20
    mymap = [[-1] * 40 for i in range(40)]
    mymap[pos[0]][pos[1]] = 0
    dist = 0
    move = 0
    for m in mymap:
        print(m)
    it = 0
    while it < 200:
        it += 1
        ic.input = move+1
        ic.run()
        if ic.state_finish:
            break
        print('try direction:',ic.input,'reply',ic.output,'pos',pos)
        if ic.output[0] == 0:
            tpos = [0,0]
            tpos[0] = pos[0]+1 if move == 2 else pos[0]-1 if move == 3 else pos[0]
            tpos[1] = pos[1]+1 if move == 0 else pos[1]-1 if move == 1 else pos[1]
            mymap[tpos[0]][tpos[1]] = -2
            print('can\'t move')
            #smart move choice
            #move = random.randint(0,3)
            move = 1
            while move < 4:
                tpos[0] = pos[0]+1 if move == 2 else pos[0]-1 if move == 3 else pos[0]
                tpos[1] = pos[1]+1 if move == 0 else pos[1]-1 if move == 1 else pos[1]
                if mymap[tpos[0]][tpos[1]] == -2:
                    print(move,tpos[0],tpos[1],mymap[tpos[0]][tpos[1]])
                    move = move+1
                else:
                    break
        else:
            print('pre-move:',pos)
            pos[0] += 1 if move == 2 else -1 if move == 3 else 0
            pos[1] += 1 if move == 0 else -1 if move == 1 else 0
            print('post-move:',pos)
            #mymap[pos[0]][pos[1]] = dist if (mymap[pos[0]][pos[1]] == -1 or mymap[pos[0]][pos[1]] > dist) else mymap[pos[0]][pos[1]]
            #dist = dist + 1 if mymap[pos[0]][pos[1]] == dist else mymap[pos[0]][pos[1]] if mymap[pos[0]][pos[1]] < dist else dist
            dist = mymap[pos[0]][pos[1]] if mymap[pos[0]][pos[1]] < dist and mymap[pos[0]][pos[1]] >= 0 else dist+1
            #dist += 1
            print('pre-location',pos,dist,mymap[pos[0]][pos[1]])
            #if mymap[pos[0]][pos[1]] < dist and mymap[pos[0]][pos[1]] >= 0:
            #    dist = mymap[pos[0]][pos[1]]
            mymap[pos[0]][pos[1]] = dist
            print('location',pos,dist,mymap[pos[0]][pos[1]])
            #move = (move-1)%4
            print('Updated map:',pos[0],pos[1],mymap[pos[0]][pos[1]])
            if ic.output[0] == 2:
                print('FOUND at distance:',mymap[pos[0]][pos[1]])
                break
        #print (mymap)
        #print(ic.output)
        #send command (1 n; 2 s; 3 w; 4 e)
        #wait for reply (0 =failed, wall; 1=moved; 2=moved, found oxygen)
        ic.output = []
        if ic.state_finish:
            break
    for m in mymap:
        print(m)

print("My data:\n", data, "\n")

print("** Part one")
print("My solution is: ", part1(data), "\n")

#print("** Part two")
#print("My solution is: ", part2(data), "\n")
