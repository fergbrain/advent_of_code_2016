import re

with open("input_day_4.txt") as f:
    room_check = f.readlines()

#room_check = ["qzmt-zixmtkozy-ivhz-343[zimth]"]
#room_check = ["aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]", "totally-real-room-200[decoy]"]

# https://inventwithpython.com/chapter14.html
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
        translated = ''
        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26

                translated += chr(num)
            else:
                translated += symbol
        return translated

alphabet = "abcdefghijklmnopqrstuvwxyz"

sector_sum = 0

for room in room_check:
    room = room.replace("-", "")
    m = re.match("([a-z]+)(\d+)\[([a-z]+)\]", room)
    enc_name = {}
    for letter in alphabet:
        enc_name[letter] = int(m.group(1).count(letter))
    sort_name = sorted(enc_name.values())
    sort_name.reverse()
    sort_name = sort_name[:5]
    #print sort_name
    #print enc_name
    checksum_pos = 0
    checksum = []
    for pos in sort_name:
        for letter in alphabet:
            if enc_name[letter] == pos:
                enc_name[letter] = -1
                checksum.extend(letter)
                break
    if m.group(3) == ''.join(checksum):
        sector_sum += int(m.group(2))
        #print m.group(1)
        print m.group(2) + ": " + getTranslatedMessage('d', m.group(1), -1*int(m.group(2)) % 26)
print "Sector sum: " + str(sector_sum)