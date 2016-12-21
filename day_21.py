import re
import numpy
import itertools

with open("input_day_21.txt") as f:
    code = f.readlines()

#code = ["swap position 4 with position 0", "swap letter d with letter b", "reverse positions 0 through 4", "rotate left 1 step", "move position 1 to position 4", "move position 3 to position 0", "rotate based on position of letter b", "rotate based on position of letter d"]

class Scramble:

    password = None

    def __init__(self, password):
        self.password = []
        for letter in password:
            self.password.append(letter)

    def read(self, operations):
        for op in operations:
                if op[:8] == "swap pos":
                    m = re.match("swap position (\d+) with position (\d+)", op)
                    self.swap_pos(m.group(1), m.group(2))
                elif op[:8] == "swap let":
                    m = re.match("swap letter (\w) with letter (\w)", op)
                    self.swap_let(m.group(1), m.group(2))
                elif op[:11] == "rotate base":
                    m = re.match("rotate based on position of letter (\w)", op)
                    self.rotate_pos(m.group(1))
                elif op[:6] == "rotate":
                    m = re.match("rotate (left|right) (\d+) step", op)
                    #print op
                    #print "Dir: %s\tSteps: %s" % (m.group(1), m.group(2))
                    self.rotate_let(m.group(1), m.group(2))
                elif op[:7] == "reverse":
                    m = re.match("reverse positions (\d+) through (\d+)", op)
                    self.reverse(m.group(1), m.group(2))
                elif op[:4] == "move":
                    m = re.match("move position (\d+) to position (\d+)", op)
                    self.move(m.group(1), m.group(2))
                else:
                    print "Missing instruction: %s" % op
                    exit()

    def swap_pos(self, x, y):
        a = self.password[int(x)]
        b = self.password[int(y)]
        self.password[int(x)] = b
        self.password[int(y)] = a

    def swap_let(self,x, y):
        for i in range(0,len(self.password)):
            if self.password[i] == x:
                self.password[i] = y
            elif self.password[i] == y:
                self.password[i] = x

    def rotate_pos(self, x):
        rotations = self.password.index(x)
        if rotations >= 4:
            rotations += 2
        else:
            rotations += 1
        self.rotate_let("right", rotations)

    def rotate_let(self, direction, x):
        if direction == "left":
            x = int(x) * -1
        elif direction == "right":
            pass
        else:
            print "Missing valid direction: %s" % direction
        self.password = list(numpy.roll(self.password, int(x)))

    def reverse(self, x, y):
        temp = list(self.password)
        j = int(y)
        for i in range(int(x), int(y)+1):
            self.password[i] = temp[j]
            j -= 1

    def move(self, x, y):
        a = self.password[int(x)]
        self.password.pop(int(x))
        # http://stackoverflow.com/questions/14895599/insert-an-element-at-specific-index-in-a-list-and-return-updated-list
        self.password = self.password[:int(y)] + [a] + self.password[int(y):]

# part 1
scramble = Scramble("abcdefgh")
scramble.read(code)
print ''.join(scramble.password)

# part 2
for it in itertools.permutations("abcdefgh", 8):
    #print "Starting %s" % ''join(list(it))
    scramble = Scramble(list(it))
    scramble.read(code)
    if ''.join(scramble.password) == "fbgdceah":
        print ''.join(list(it))
        break
