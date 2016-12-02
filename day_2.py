from math import sqrt, pow


class Pad:

    position = []

    def __init__(self):
        self.set_number(5)

    def move_up(self):
        if self.position[1] < 1:
            self.position[1] += 1

    def move_down(self):
        if self.position[1] > -1:
            self.position[1] -= 1

    def move_left(self):
        if self.position[0] > -1:
            self.position[0] -= 1

    def move_right(self):
        if self.position[0] < 1:
            self.position[0] += 1

    def set_number(self, num):
        if num == 1:
            self.position = [-1, 1]
        elif num == 2:
            self.position = [0, 1]
        elif num == 3:
            self.position = [1, 1]
        elif num == 4:
            self.position = [-1, 0]
        elif num == 5:
            self.position = [0, 0]
        elif num == 6:
            self.position = [1, 0]
        elif num == 7:
            self.position = [-1, -1]
        elif num == 8:
            self.position = [0, -1]
        elif num == 9:
            self.position = [1, -1]
        else:
            pass  # error

    def get_number(self):
        if self.position == [-1, 1]:
            return 1
        elif self.position == [0, 1]:
            return 2
        elif self.position == [1, 1]:
            return 3
        elif self.position == [-1, 0]:
            return 4
        elif self.position == [0, 0]:
            return 5
        elif self.position == [1, 0]:
            return 6
        elif self.position == [-1, -1]:
            return 7
        elif self.position == [0, -1]:
            return 8
        elif self.position == [1, -1]:
            return 9
        else:
            pass  # error


class Pad2:

    position = []

    def __init__(self):
        self.set_number("5")

    def move_up(self):
        if sqrt(pow(self.position[0], 2) + pow(self.position[1], 2)) < 1.4 or \
                self.position[1] < 0:
            self.position[1] += 1

    def move_down(self):
        if sqrt(pow(self.position[0], 2) + pow(self.position[1], 2)) < 1.4 or \
                self.position[1] > 0:
            self.position[1] -= 1

    def move_left(self):
        if sqrt(pow(self.position[0], 2) + pow(self.position[1], 2)) < 1.4 or \
                self.position[0] > 0:
            self.position[0] -= 1

    def move_right(self):
        if sqrt(pow(self.position[0], 2) + pow(self.position[1], 2)) < 1.4 or \
                self.position[0] < 0:
            self.position[0] += 1

    def set_number(self, num):
        if num == "2":
            self.position = [-1, 1]
        elif num == "3":
            self.position = [0, 1]
        elif num == "4":
            self.position = [1, 1]
        elif num == "6":
            self.position = [-1, 0]
        elif num == "7":
            self.position = [0, 0]
        elif num == "8":
            self.position = [1, 0]
        elif num == "A":
            self.position = [-1, -1]
        elif num == "B":
            self.position = [0, -1]
        elif num == "C":
            self.position = [1, -1]
        elif num == "5":
            self.position = [-2, 0]
        elif num == "9":
            self.position = [2, 0]
        elif num == "1":
            self.position = [0, 2]
        elif num == "D":
            self.position = [0, -2]

        else:
            pass  # error

    def get_number(self):
        if self.position == [-1, 1]:
            return "2"
        elif self.position == [0, 1]:
            return "3"
        elif self.position == [1, 1]:
            return "4"
        elif self.position == [-1, 0]:
            return "6"
        elif self.position == [0, 0]:
            return "7"
        elif self.position == [1, 0]:
            return "8"
        elif self.position == [-1, -1]:
            return "A"
        elif self.position == [0, -1]:
            return "B"
        elif self.position == [1, -1]:
            return "C"
        elif self.position == [-2, 0]:
            return "5"
        elif self.position == [2, 0]:
            return "9"
        elif self.position == [0, 2]:
            return "1"
        elif self.position == [0, -2]:
            return "D"
        else:
            pass  # error


# instr = ["ULL", "RRDDD", "LURDL", "UUUUD"]

with open("input_day_2.txt") as f:
    instr = f.readlines()

pad = Pad2()

for line in instr:
    for move in line:
        if move == "U":
            pad.move_up()
        elif move == "D":
            pad.move_down()
        elif move == "L":
            pad.move_left()
        elif move == "R":
            pad.move_right()
        else:
            pass  # error
    print str(pad.get_number())