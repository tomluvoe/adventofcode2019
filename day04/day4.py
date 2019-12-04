#!/usr/bin/python3

data = "206938-679128"

def password_p1(key):
    keys = str(key)
    dbl = False
    for i in range(len(keys)-1):
        if keys[i] > keys[i+1]:
            return False
        if keys[i] == keys[i+1]:
            dbl = True
    return dbl

def password_p2(key):
    keys = str(key)
    dbl = False
    dbln = -2
    for i in range(len(keys)-1):
        if keys[i] > keys[i+1]:
            return False
        if keys[i] == keys[i+1]:
            if dbl > i-2:
                dbl = i
                dbl = False
            else:
                dbl = True
    return dbl

def part1(data):
    pwd = 0
    x0,x1 = data.split('-')
    for i in range(int(x1)-int(x0)):
        if password_p1(i+int(x0)) == True:
            pwd += 1
    return pwd


def unit_test_p1():
    print("Unit test start:")
    assert password_p1(111111) == True
    print("Test 1 OK")
    assert password_p1(223450) == False
    print("Test 2 OK")
    assert password_p1(123789) == False
    print("Test 3 OK")

def unit_test_p2():
    print("Unit test start:")
    assert password_p2(112233) == True
    print("Test 1 OK")
    assert password_p2(123444) == False
    print("Test 2 OK")
    assert password_p2(111122) == True
    print("Test 3 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is: ", part1(data), "\n")
