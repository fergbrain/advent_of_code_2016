import pprint
import re
import numpy as np
import sys

with open("input_day_8.txt") as f:
    code = f.readlines()

#code = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"]

np.set_printoptions(linewidth=120)

class Buffer:
    z = None
    #x = None
    #y = None

    def __init__(self, x=0, y=0):
        pass
        print "Init: %s x %s" % (x, y)
        self.z = np.zeros((y, x), dtype=int)

        #self.z = np.array()

    def runBuff(self, code):
        for line in code:
            instruct = line.split(" ",1)
            if instruct[0] == "rect":
                self.rect(int(instruct[1].split("x")[0]), int(instruct[1].split("x")[1]))
            elif instruct[0] == "rotate":
                m = re.match("(row|column) (?:x|y)\=(\d+) by (\d+)", instruct[1])
                self.rotate(str(m.group(1)), int(m.group(2)), int(m.group(3)))
            else:
                print "Invalid instruction: " + str(line)
                exit()
            #print instruct

    def rect(self, x, y):
        fill = [x, y]
        print "Fill: %s " % fill
        resize = False
        if self.z.shape[1] < x:
            resize = True
        else:
            x = self.z.shape[0]
        if self.z.shape[0] < y:
            resize = True
        else:
            y = self.z.shape[1]

        if resize:
            #print "Resizing to: %s" % ([x,y])
            self.z = np.resize(self.z, (y, x))
            #print self.z

        for j in range(0, fill[1]):
            for i in range(0, fill[0]):
                self.z[j][i] = 1

        self.printBuf()

    def rotate(self, type, a, b):
        if type == "row":
            print "Rotate row %s by %s" % (a, b)
            rowBuf = np.copy(self.z[a])
            print rowBuf
            for i in range(0, len(rowBuf)):
                #print "Buffer: %s" % rowBuf
                #print "Array : %s" % self.z[a]
                if i + b < len(rowBuf):
                    #print "%s:%s:%s" % ((i + b), rowBuf[i], i)
                    self.z[a][i + b] = rowBuf[i]
                else:
                    #print "%s:%s:%s" % ((i - len(rowBuf) + b), rowBuf[i], i)
                    self.z[a][i - len(rowBuf) + b] = rowBuf[i]
        elif type == "column":
            print "Rotate column %s by %s" % (a, b)
            rowBuf = np.copy(self.z[:,a])
            print rowBuf
            for i in range(0, len(rowBuf)):
                # print "Buffer: %s" % rowBuf
                # print "Array : %s" % self.z[a]
                if i + b < len(rowBuf):
                    # print "%s:%s:%s" % ((i + b), rowBuf[i], i)
                    self.z[i + b][a] = rowBuf[i]
                else:
                    # print "%s:%s:%s" % ((i - len(rowBuf) + b), rowBuf[i], i)
                    self.z[i - len(rowBuf) + b][a] = rowBuf[i]
        else:
            print "Error: invalid type %s" % type
            exit()
        #print "Type: %s\nA: %s\nB: %s" % (type, x, y)

    def printBuf(self):
        count = 0
        for line in self.z:
            for char in line:
                if char == 0:
                    sys.stdout.write(" ")
                elif char == 1:
                    sys.stdout.write("#")
                    count += 1
            sys.stdout.write("\n")
        print "Pixels: %s" % count


#buf = Buffer(7, 3)
buf = Buffer(50,6)
buf.runBuff(code)
buf.printBuf()