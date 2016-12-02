import re
import numpy as np
import pylab as pl
from matplotlib import collections  as mc

routeInput = "L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1"
routeSteps = routeInput.split(",")


class Nav:

    direction = None
    location = [None, None]
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    history = []

    def __init__(self):
        self.location = [0, 0]
        self.history.append(self.location[:])
        self.direction = self.NORTH

    def rotate_ccw(self):
        if self.direction == self.NORTH:
            self.direction = self.WEST
        elif self.direction == self.EAST:
            self.direction = self.NORTH
        elif self.direction == self.SOUTH:
            self.direction = self.EAST
        elif self.direction == self.WEST:
            self.direction = self.SOUTH
        else:
            pass  # error
        # print "Rotate :: CCW - " + str(self.direction) # debug

    def rotate_cw (self):
        if self.direction == self.NORTH:
            self.direction = self.EAST
        elif self.direction == self.EAST:
            self.direction = self.SOUTH
        elif self.direction == self.SOUTH:
            self.direction = self.WEST
        elif self.direction == self.WEST:
            self.direction = self.NORTH
        else:
            pass  # error
        # print "Rotate :: CW - " + str(self.direction) #debug

    def move(self, blocks):
        if self.direction == self.NORTH:
            self.location[0] = self.location[0] + blocks
        elif self.direction == self.EAST:
            self.location[1] = self.location[1] + blocks
        elif self.direction == self.SOUTH:
            self.location[0] = self.location[0] - blocks
        elif self.direction == self.WEST:
            self.location[1] = self.location[1] - blocks
        else:
            pass # error

    def segment_check(self):
        for i in range(1, len(nav.history)):

            p1 = np.array([float(self.location[0]), float(self.location[1])])
            p2 = np.array([float(self.history[len(self.history)-1][0]), float(self.history[len(self.history)-1][1])])

            p3 = np.array([float(self.history[i][0]), float(self.history[i][1])])
            p4 = np.array([float(self.history[i-1][0]), float(self.history[i-1][1])])


            intersect = self.seg_intersect(p1, p2, p3, p4)

            if not isinstance(intersect,bool):

                if ( min(self.history[i-1][0], self.history[i][0]) <= intersect[0] <= max(self.history[i-1][0], self.history[i][0]) and \
                        min(self.history[i-1][1], self.history[i][1]) <= intersect[1] <= max(self.history[i-1][1], self.history[i][1]) ) and \
                        (min(self.location[0], self.history[len(self.history)-1][0]) <= intersect[0] <= max(self.location[0], self.history[len(self.history)-1][0]) and \
                            min(self.location[1], self.history[len(self.history)-1][1]) <= intersect[1] <= max(self.location[1], self.history[len(self.history)-1][1])) and \
                                i < len(self.history)-2:

                    # print "Between " + str(p1) + str(p2) # debug
                    # print "Between " + str(p3) + str(p4) # debug
                    # print "Between: " + str(self.history[i - 1]) + " and " + str(self.history[i]) # debug
                    # print str(self.history[i][0]) + " >= " + str(self.location[0]) + " >= " + str(self.history[i - 1][0]) # debug
                    # print str(self.history[i][1]) + " >= " + str(self.location[1]) + " >= " + str(self.history[i - 1][1]) # debug
                    # print "Sequence: " + str(i) # debug
                    # print "Direction: " + str(self.direction) # debug
                    # print "Location: " + str(self.location) # debug
                    print "Blocks: " + str(abs(intersect[0]) + abs(intersect[1])) #answer

                    # print self.location # debug
                    # print self.history # debug

                    # easy visual check of the solution
                    '''
                    lc = mc.LineCollection(lines, linewidths=2)
                    fig, ax = pl.subplots()
                    ax.add_collection(lc)
                    ax.autoscale()
                    ax.margins(0.1)
                    pl.show()
                    '''
                    exit()



    # http://www.cs.mun.ca/~rod/2500/notes/numpy-arrays/numpy-arrays.html
    def perp(self, a):
        b = np.empty_like(a)
        b[0] = -a[1]
        b[1] = a[0]
        return b

    def seg_intersect(self, a1, a2, b1, b2):
        da = a2 - a1
        db = b2 - b1
        dp = a1 - b1
        dap = self.perp(da)
        denom = np.dot(dap, db)
        num = np.dot(dap, dp)
        if denom == 0.:
            return False
        else:
            return (num / denom) * db + b1

nav = Nav()
i = 0
lines = []
for seq in routeSteps:
    i += 1
    m = re.match(".*?(R|L)(\d*).*?", seq)
    rotation = str(m.group(1))
    steps = int(m.group(2))
    if rotation == "L":
        nav.rotate_ccw()
        nav.move(steps)
    elif rotation == "R":
        nav.rotate_cw()
        nav.move(steps)
    else:
        pass  # error

    prev_point = ( nav.history[len(nav.history)-1][0], nav.history[len(nav.history)-1][1] )
    this_point = ( nav.location[0], nav.location[1])
    lines.append([prev_point, this_point])
    nav.segment_check()
    nav.history.append(nav.location[:])

print "Direction: " + str(nav.direction)
print "Location: " + str(nav.location)
print "Blocks: " + str(abs(nav.location[0]) + abs(nav.location[1]))