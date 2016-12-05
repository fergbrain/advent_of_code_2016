import hashlib
import sys


def RepresentsInt(s): # http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
    try:
        int(s)
        return True
    except ValueError:
        return False


def spinning_cursor(): # http://stackoverflow.com/questions/4995733/how-to-create-a-spinning-command-line-cursor-using-python
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()

puzzle_input = "ugkcyxxp"
i = 0
password = {0: None,
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None}
done = False


def print_password(password):
    for pos, letter in password.iteritems():
        if letter is None:
            letter = spinner.next()
        sys.stdout.write(str(letter))

while not done:
    if i % 100000 == 0:
        pass
        sys.stdout.write("\r")
        print_password(password)

    thisHash = hashlib.md5(puzzle_input + str(i)).hexdigest()

    if thisHash[:5] == "00000" and RepresentsInt(thisHash[5:6]):
        if int(thisHash[5:6]) < 8 and password[int(thisHash[5:6])] is None:
            password[int(thisHash[5:6])] = thisHash[6:7]
            if all(letter is not None for letter in password.values()):
                    done = True
        sys.stdout.write("\r")
        print_password(password)
        if done:
            print " ...done"
    i += 1