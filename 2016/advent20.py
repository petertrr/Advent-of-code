import time
INT_MAX = 2**32

start_time = time.time()
task = open('advent20.txt', 'r')
line = task.readline()
blocked = [[int(line.split('-')[0]), 0], [int(line.split('-')[1]), 1]]
while True:
    line = task.readline()
    if len(line) == 0:
        break
    blocked += [[int(line.split('-')[0]), 0], [int(line.split('-')[1]), 1]]
    blocked.sort()

ranges = []
zeros, ones = 0, 0
left = blocked[0][0]
for i in range(0, len(blocked)):
    if blocked[i][1] == 0:
        zeros += 1
    else:
        ones += 1
    if zeros == ones:
        ranges.append([left, blocked[i][0]])
        zeros, ones = 0, 0
        if i + 1 < len(blocked):
            left, right = blocked[i + 1][0], 0
    i += 1

i = 0
while i < len(ranges) - 1:
    if ranges[i][1] + 1 == ranges[i + 1][0]:
        ranges[i][1] = ranges[i + 1][1]
        ranges.pop(i + 1)
    else:
        i += 1
print("Lowest ip is %d" % (ranges[0][1] + 1))

ip, count = 0, 0
for i in range(0, len(ranges)):
    if ip == ranges[i][0]:
        ip = ranges[i][1] + 1
        i += 1
    else:
        ip += 1
        count += 1
print("%d ips allowed" % count)
elapsed_time = time.time() - start_time
print("%.3f seconds passed" % elapsed_time)