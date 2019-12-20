#!/usr/bin/python3

class intcode():

    cmd_str = ['','+','*']

    def __init__(self,data,input=0,state_wait=True):
        self.data = list(map(int, data.split(',')))
        self.input = input
        self.pc = 0
        self.rb = 0
        self.output = []
        self.state_wait = False
        self.state_wait_when_output = state_wait
        self.input_to = 0
        self.state_finish = False
        self.ic = 0

    def state(self):
        print("Status:")
        print("->PC",self.pc)
        print("->SW",self.state_wait)
        print("->SWO",self.state_wait_when_output)
        print("->SF",self.state_finish)
        print("->IN",self.input)
        print("->IT",self.input_to)
        print("->OUT",self.output)

    def ext_data_buffer(self, addr):
        if addr > len(self.data) - 1:
            self.data.extend([0]*(addr - len(self.data) + 1))

    def param_mode(self):
        pm = '00'
        p1 = 0
        p2 = 0
        pc = self.pc

        instr = int(self.data[pc])
        if len(str(instr)) > 2:
            instr = int(str(self.data[pc])[-2:])
            pm = '00'+str(self.data[pc])[:-2]
        if pm[-1] == '0':
            self.ext_data_buffer(self.data[pc+1])
            p1 = self.data[self.data[pc+1]]
        elif pm[-1] == '1':
            p1 = self.data[pc+1]
        else:
            self.ext_data_buffer(self.data[pc+1]+self.rb)
            p1 = self.data[self.data[pc+1]+self.rb]
        if instr < 3 or (instr > 4 and instr < 9):
            if pm[-2] == '0':
                self.ext_data_buffer(self.data[pc+2])
                p2 = self.data[self.data[pc+2]]
            elif pm[-2] == '1':
                p2 = self.data[pc+2]
            else:
                self.ext_data_buffer(self.data[pc+2]+self.rb)
                p2 = self.data[self.data[pc+2]+self.rb]
        if instr == 3:
            if pm[-1] == '0':
                if type(self.input) == int:
                    p1 = self.input
            elif pm[-1] == '1':
                if type(self.input) == int:
                    p1 = self.input
            else:
                if type(self.input) == int:
                    #TODO: CHANGE ADDR??
                    self.ext_data_buffer(self.input+self.rb)
                    p1 = self.data[self.input+self.rb]
        return instr,p1,p2

    def step(self):
        pc = self.pc
        dat = self.data

        instr,p1,p2 = self.param_mode()
        instr = int(str(self.data[pc])[-2:])
        mode = '000'+str(self.data[pc])[:-2]

        if(instr < 3):
            p3 = self.data[pc+3] if mode[-3] == '0' else pc+3 if mode[-3] == '1' else self.data[pc+3]+self.rb
            self.ext_data_buffer(p3)
            dat[p3] = eval(str(p1)+self.cmd_str[instr]+str(p2))
            pc += 4
        elif(instr == 3):
            self.ext_data_buffer(dat[pc+1])
            if type(self.input) == int:
                dat[dat[pc+1]] = p1
                if str(self.data[pc])[:-2] == '2':
                    dat[dat[pc+1]+self.rb] = self.input
            else:
                dat[dat[pc+1]] = self.input[self.ic]
                self.ic = (self.ic + 1)%len(self.input)
            pc += 2
        elif(instr == 4):
            self.output.append(p1)
            if self.state_wait_when_output:
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
            p3 = self.data[pc+3] if mode[-3] == '0' else pc+3 if mode[-3] == '1' else self.data[pc+3]+self.rb
            self.ext_data_buffer(p3)
            if p1 < p2:
                dat[p3] = 1
            else:
                dat[p3] = 0
            pc += 4
        elif(instr == 8):
            p3 = self.data[pc+3] if mode[-3] == '0' else pc+3 if mode[-3] == '1' else self.data[pc+3]+self.rb
            self.ext_data_buffer(p3)
            if p1 == p2:
                dat[p3] = 1
            else:
                dat[p3] = 0
            pc += 4
        elif(instr == 9):
            self.rb += p1
            pc += 2
        self.data = dat
        self.pc = pc

    def run(self):
        self.state_wait = False
        while self.data[self.pc] != 99 and not self.state_wait:
            self.step()
        if self.data[self.pc] == 99:
            self.state_finish = True

def test_day2_p1():
    print("Unit test start day2:")
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
    print(ic.data)
    assert ic.data == [30,1,1,4,2,5,6,0,99]
    print("Test 4 OK")
    ic = intcode("1,9,10,3,2,3,11,0,99,30,40,50",0)
    ic.run()
    assert ic.data == [3500,9,10,70,2,3,11,0,99,30,40,50]
    print("Test 5 OK")

def test_day5_p1():
    print("Unit test start day5 p1:")
    ic = intcode("1002,4,3,4,33",0)
    ic.run()
    assert ic.data == [1002,4,3,4,99]
    print("Test 1 OK")
    ic = intcode("1101,100,-1,4,0",0)
    ic.run()
    assert ic.data == [1101,100,-1,4,99]
    print("Test 2 OK")

def test_day5_p2():
    print("Unit test start day5 p2;")
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
    test_data = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    ic = intcode(test_data,0)
    ic.run()
    assert ic.output[-1] == 0
    print("Test 4 OK")
    ic = intcode(test_data,7)
    ic.run()
    assert ic.output[-1] == 1
    print("Test 5 OK")
    test_data = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    ic = intcode(test_data,0)
    ic.run()
    assert ic.output[-1] == 0
    print("Test 6 OK")
    ic = intcode(test_data,7)
    ic.run()
    assert ic.output[-1] == 1
    print("Test 7 OK")

def thrusters(data,phase):
    thrust = 0
    for a in range(5):
        amp = intcode(data,[phase[a],thrust])
        amp.run()
        thrust = amp.output[-1]
    return thrust

def thrusters_w_feedback(data,phase):
    thrust = 0
    amps = []
    for a in range(5):
        amps.append(intcode(data,[phase[a],thrust]))
        amps[a].run()
        thrust = amps[a].output[-1]
    while not amps[4].state_finish:
        for a in range(5):
            amps[a].input = thrust
            amps[a].run()
            thrust = amps[a].output[-1]
    return thrust

def test_day7_p1():
    print("Unit test start day7 p1;")
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
    print("Unit test start day7 p2;")
    test_data = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    assert thrusters_w_feedback(test_data,[9,8,7,6,5]) == 139629729
    print("Test 1 OK")
    test_data = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    assert thrusters_w_feedback(test_data,[9,7,8,5,6]) == 18216
    print("Test 2 OK")

def test_day9_p1():
    print("Unit test start day9 p1;")
    test_data = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    ic = intcode(test_data,0)
    ic.state_wait_when_output = False
    ic.run()
    assert ic.output == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    print("Test 1 OK")
    test_data = "1102,34915192,34915192,7,4,7,99,0"
    ic = intcode(test_data,1)
    ic.run()
    assert len(str(ic.output[0])) == 16
    print("Test 2 OK")
    test_data = "104,1125899906842624,99"
    ic = intcode(test_data,1)
    ic.run()
    assert ic.output[0] == 1125899906842624
    print("Test 3 OK")

test_day2_p1()
test_day5_p1()
test_day5_p2()
test_day7_p1()
test_day7_p2()
test_day9_p1()
