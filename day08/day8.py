#!/usr/bin/python3

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1]

def part1(data,imgsize):
    size = imgsize[0]*imgsize[1]
    min_zeros = size
    result = 0
    for i in range(len(data)//size):
        if data[i*size:i*size+size].count('0') < min_zeros:
            min_zeros = data[i*size:i*size+size].count('0')
            result = data[i*size:i*size+size].count('1') * data[i*size:i*size+size].count('2')
    return result

def part2(data,imgsize):
    size = imgsize[0]*imgsize[1]
    result = '2'*size
    for layer in range(len(data)//size):
        for pix in range(size):
            if result[pix] == '2':
                result = result[:pix]+data[layer*size+pix]+result[pix+1:]
    for r in range(imgsize[1]):
        for pix in range(imgsize[0]):
            if result[r*imgsize[0]+pix] == '1':
                print('1', end='')
            else:
                print(' ', end='')
        print('')
    return result

def test_day8_p1():
    print("Unit test start day8 p1:")
    assert part1("123456789012",[3,2]) == 1
    print("Test 1 OK")

def test_day8_p2():
    print("Unit test start day8 p2:")
    assert part2("0222112222120000",[2,2]) == '0110'
    print("Test 2 OK")

print("My data:\n", data, "\n")

print("** Part one")
test_day8_p1()
print("My solution is: ", part1(data,[25,6]), "\n")

print("** Part one")
test_day8_p2()
print("My solution is: ", part2(data,[25,6]), "\n")
