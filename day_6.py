with open("input_day_6.txt") as f:
    message_list = f.readlines()

alphabet = "abcdefghijklmnopqrstuvwxyz"

corrected_message = {   0: {},
                        1: {},
                        2: {},
                        3: {},
                        4: {},
                        5: {},
                        6: {},
                        7: {}}

for message in message_list:
    for i in range(0,8):
        j = message[i]
        if j in corrected_message[i]:
            corrected_message[i][j] += 1
        else:
            corrected_message[i][j] = 1

for key, position in corrected_message.iteritems():
    for letter, count in position.iteritems():
        if count == min(sorted(position.values())): #or max()
            print letter