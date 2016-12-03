import re

with open("input_day_3.txt") as f:
    triangle_list = f.readlines()

count = 0
for sides in triangle_list:
    print "Testing: " + str(sides)
    m = re.match(".*?(\d+)\s+(\d+)\s+(\d+)", sides)
    if (int(m.group(1)) + int(m.group(2))) > int(m.group(3)) and \
            int(m.group(1)) + int(m.group(3)) > int(m.group(2)) and \
            int(m.group(2)) + int(m.group(3)) > int(m.group(1)):
        count += 1

print "Part 1 count: " + str(count)


count = 0
for i in range(2, len(triangle_list), 3):

    m1 = re.match(".*?(\d+)\s+(\d+)\s+(\d+)", triangle_list[i-2])
    m2 = re.match(".*?(\d+)\s+(\d+)\s+(\d+)", triangle_list[i-1])
    m3 = re.match(".*?(\d+)\s+(\d+)\s+(\d+)", triangle_list[i])

    for j in range(1,4):
        print "Testing: " + str(m1.group(j)) + "  " + str(m2.group(j)) + "  "  + str(m3.group(j))
        if (int(m1.group(j)) + int(m2.group(j))) > int(m3.group(j)) and \
                int(m1.group(j)) + int(m3.group(j)) > int(m2.group(j)) and \
                int(m2.group(j)) + int(m3.group(j)) > int(m1.group(j)):
            count += 1

print "Part 2 count: " + str(count)
