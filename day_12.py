

class Assembunny:
    regA = None
    regB = None
    regC = None
    regD = None
    pc = None
    cycle = None

    def __init__(self):
        self.regA = 0
        self.regB = 0
        self.regC = 1 # part two initializes this to 1
        self.regD = 0
        self.pc = 0
        self.cycle = 0

    def runAssem(self, code):
        while self.pc < len(code):
            self.cycle += 1
            #print "A: %s, B: %s, C: %s, D: %s, PC: %s, Cycle: %s" % (self.regA, self.regB, self.regC, self.regD, self.pc, self.cycle)
            instruct = code[self.pc].split()
            if instruct[0] == "cpy":
                self.cpy(instruct[1], instruct[2])
            elif instruct[0] == "inc":
                self.inc(instruct[1])
            elif instruct[0] == "dec":
                self.dec(instruct[1])
            elif instruct[0] == "jnz":
                self.jnz(instruct[1], instruct[2])

    def cpy(self, x, y):
        try:
            x = int(x)
        except ValueError:
            pass

        if isinstance(x, str):
            if x == "a":
                x = self.regA
            elif x == "b":
                x = self.regB
            elif x == "c":
                x = self.regC
            elif x == "d":
                x = self.regD
            else:
                print "Error: undefined x register - " + str(x) + " @ PC: " + str(self.pc)
                exit()

        if isinstance(x, int):
            if y == "a":
                self.regA = x
            elif y == "b":
                self.regB = x
            elif y == "c":
                self.regC = x
            elif y == "d":
                self.regD = x
            else:
                print "Error: undefined y register - " + str(y) + " @ PC: " + str(self.pc)
                exit()
        else:
            print "Error: cpy failed"
            exit()

        self.pc += 1

    def inc(self, x):
        if isinstance(x, str):
            if x == "a":
                self.regA += 1
            elif x == "b":
                self.regB += 1
            elif x == "c":
                self.regC += 1
            elif x == "d":
                self.regD += 1
            else:
                print "Error: undefined x register - " + str(x) + " @ PC: " + str(self.pc)
                exit()
        else:
            print "Error: inc failed"
            exit()

        self.pc += 1

    def dec(self, x):
        if isinstance(x, str):
            if x == "a":
                self.regA -= 1
            elif x == "b":
                self.regB -= 1
            elif x == "c":
                self.regC -= 1
            elif x == "d":
                self.regD -= 1
            else:
                print "Error: undefined x register - " + str(x) + " @ PC: " + str(self.pc)
                exit()
        else:
            print "Error: dec failed"
            exit()

        self.pc += 1

    def jnz(self, x, y):
        try:
            x = int(x)
        except ValueError:
            pass

        if isinstance(x, str):
            if x == "a":
                x = self.regA
            elif x == "b":
                x = self.regB
            elif x == "c":
                x = self.regC
            elif x == "d":
                x = self.regD
            else:
                print "Error: undefined x register - " + str(x) + " @ PC: " + str(self.pc)
                exit()
        elif isinstance(x, int):
            pass
        else:
            print "Error: jnz failed"
            exit()
        if x != 0:
            self.pc += int(y)
        else:
            self.pc += 1


with open("input_day_12.txt") as f:
    code = f.readlines()

asm = Assembunny()

asm.runAssem(code)
print "A: %s, B: %s, C: %s, D: %s, PC: %s, Cycle: %s" % (asm.regA, asm.regB, asm.regC, asm.regD, asm.pc, asm.cycle)

