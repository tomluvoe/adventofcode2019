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
    dbld = [-1,-1]
    dbln = -2
    for i in range(len(keys)-1):
        if keys[i] > keys[i+1]:
            return False
        if keys[i] == keys[i+1]:
            if dbln == i-1:
                if dbld[0] == keys[i] and dbld[1] == i-1:
                    dbl = False
                    dbld = [-1,-1]
            else:
                if dbld[0] == -1 or dbld[1] == i-1:
                    dbl = True
                    dbld = [keys[i],i]
            dbln = i
    return dbl

def part12(data, fcn):
    pwd = 0
    x0,x1 = data.split('-')
    for i in range(int(x1)-int(x0)+1):
        if eval(fcn+"(i+int(x0)) == True"):
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
    assert password_p2(112222) == True
    print("Test 4 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part12(data, 'password_p1'), "\n")

print("** Part two")
unit_test_p2()
print("My solution is: ", part12(data, 'password_p2'), "\n")
