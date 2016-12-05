import hashlib

puzzle_input = "ugkcyxxp"
i = 0
password = []

while len(password) < 8:
    if hashlib.md5(puzzle_input + str(i)).hexdigest()[:5] == "00000":
        print str(i) + ": " + str(hashlib.md5(puzzle_input + str(i)).hexdigest())
        password.append(hashlib.md5(puzzle_input + str(i)).hexdigest()[5:6])
    i += 1

print ''.join(password)

