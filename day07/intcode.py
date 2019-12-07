#!/usr/bin/python3

class intcode():

    cmd_str = ['','+','*']

    def __init__(self,data,input=0):
        self.data = list(map(int, data.split(',')))
        self.input = input
        self.pc = 0
        self.output = []
        self.break_for_input = False
        self.state_wait = False
        self.input_to = 0
        self.state_finish = False
        self.ic = 0

    def state(self):
        print("Status:")
        print("->PC",self.pc)
        print("->SW",self.state_wait)
        print("->SE",self.state_finish)
        print("->BFI",self.break_for_input)
        print("->IN",self.input)
        print("->IT",self.input_to)
        print("->OUT",self.output)

    def step(self):
        pc = self.pc
        dat = self.data
        pm = '00'
        p1 = 0
        p2 = 0

        instr = int(dat[pc])
        if len(str(instr)) > 2:
            instr = int(str(dat[pc])[-2:])
            pm = '00'+str(dat[pc])[:-2]
        if pm[-1] == '0':
            p1 = dat[dat[pc+1]]
        else:
            p1 = dat[pc+1]
        if instr < 3 or instr > 4:
            if pm[-2] == '0':
                p2 = dat[dat[pc+2]]
            else:
                p2 = dat[pc+2]
        if(instr < 3):
            dat[dat[pc+3]] = eval(str(p1)+self.cmd_str[instr]+str(p2))
            pc += 4
        elif(instr == 3):
            #if self.break_for_input:
            #    self.state_wait = True
            #    self.input_to = dat[pc+1]
            #    return
            if type(self.input) == int:
                dat[dat[pc+1]] = self.input
            else:
                dat[dat[pc+1]] = self.input[self.ic]
                self.ic = (self.ic + 1)%len(self.input)
                #self.break_for_input = True
            pc += 2
        elif(instr == 4):
            print(p1)
            self.output.append(p1)
            print ("-> break?",p1)
            self.state_wait = True
            pc += 2
        elif(instr == 5):
            if p1 == 0:
                pc += 3
            else:
                pc = p2
        elif(instr == 6):
            if p1 == 0:
                pc = p2
            else:
                pc += 3
        elif(instr == 7):
            if p1 < p2:
                dat[dat[pc+3]] = 1
            else:
                dat[dat[pc+3]] = 0
            pc += 4
        elif(instr == 8):
            if p1 == p2:
                dat[dat[pc+3]] = 1
            else:
                dat[dat[pc+3]] = 0
            pc += 4
        self.data = dat
        self.pc = pc

    def run(self):
        if self.state_wait:
            self.data[self.input_to] = self.input
            self.state_wait = False
            self.break_for_input = True
        while self.data[self.pc] != 99 and not self.state_wait:
            self.step()
        if self.data[self.pc] == 99:
            self.state_finish = True

def test_day2_p1():
    print("Unit test start:")
    ic = intcode("1,0,0,0,99",0)
    ic.run()
    assert ic.data == [2,0,0,0,99]
    print("Test 1 OK")
    ic = intcode("2,3,0,3,99",0)
    ic.run()
    assert ic.data == [2,3,0,6,99]
    print("Test 2 OK")
    ic = intcode("2,4,4,5,99,0",0)
    ic.run()
    assert ic.data == [2,4,4,5,99,9801]
    print("Test 3 OK")
    ic = intcode("1,1,1,4,99,5,6,0,99",0)
    ic.run()
    assert ic.data == [30,1,1,4,2,5,6,0,99]
    print("Test 4 OK")
    ic = intcode("1,9,10,3,2,3,11,0,99,30,40,50",0)
    ic.run()
    assert ic.data == [3500,9,10,70,2,3,11,0,99,30,40,50]
    print("Test 5 OK")

def test_day5_p1():
    print("Unit test start:")
    ic = intcode("1002,4,3,4,33",0)
    ic.run()
    assert ic.data == [1002,4,3,4,99]
    print("Test 1 OK")
    ic = intcode("1101,100,-1,4,0",0)
    ic.run()
    assert ic.data == [1101,100,-1,4,99]
    print("Test 2 OK")

def test_day5_p2():
    print("Unit test start;")
    test_data = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    ic = intcode(test_data,1)
    ic.run()
    assert ic.output[-1] == 999
    print("Test 1 OK")
    ic = intcode(test_data,8)
    ic.run()
    assert ic.output[-1] == 1000
    print("Test 2 OK")
    ic = intcode(test_data,9)
    ic.run()
    assert ic.output[-1] == 1001
    print("Test 3 OK")

def thrusters(data,phase):
    thrust = 0
    for a in range(5):
        amp = intcode(data,[phase[a],thrust])
        amp.run()
        #amp.state()
        #amp.input = thrust
        #while not amp.state_finish:
        #    amp.state_wait = False
        #    amp.run()
        #amp.state()
        thrust = amp.output[-1]
    return thrust

def thrusters_w_feedback(data,phase):
    thrust = 0
    amps = []
    for a in range(5):
        amps.append(intcode(data,[phase[a],thrust]))
        amps[a].run()
        #print(a,amps[a].input)
        thrust = amps[a].output[-1]
        #print('thrust amp',a,'loop 0 :',amps[a].state())
    print('init done')
    for l in range(10):
        for a in range(5):
            print('run again',a)
            amps[a].state_wait = False
            amps[a].input = [thrust,thrust]
            #print(a,amps[a].input)
            amps[a].run
            thrust = amps[a].output[-1]
            #print('thrust amp',a,'loop',l+1,':',amps[a].state())
    return thrust

def test_day7_p1():
    print("Unit test start;")
    test_data = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
    assert thrusters(test_data,[4,3,2,1,0]) == 43210
    print("Test 1 OK")
    test_data = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
    assert thrusters(test_data,[0,1,2,3,4]) == 54321
    print("Test 2 OK")
    test_data = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
    assert thrusters(test_data,[1,0,4,3,2]) == 65210
    print("Test 3 OK")

def test_day7_p2():
    print("Unit test start;")
    test_data = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    assert thrusters_w_feedback(test_data,[9,8,7,6,5]) == 139629729
    print("Test 1 OK")
    test_data = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    assert thrusters_w_feedback(test_data,[9,7,8,5,6]) == 18216
    print("Test 2 OK")

test_day2_p1()
test_day5_p1()
test_day5_p2()
test_day7_p1()
test_day7_p2()
