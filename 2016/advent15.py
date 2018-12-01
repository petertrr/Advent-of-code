import time

test_disks = {1: [4, 5], 2: [1, 2]}
real_disks = {1: [1, 13], 2: [10, 19], 3: [2, 3], 4: [1, 7], 5: [3, 5], 6: [5, 17], 7: [0, 11]}
disks = real_disks


def result(level, time):
    if (time + 1 - disks[level][1] + disks[level][0]) % disks[level][1] == 0:
        if level == len(disks):
            return 1
        else:
            return result(level + 1, time + 1)
    else:
        return -1

start_time = time.time()
t = disks[1][1] - disks[1][0]
while True:
    res = result(2, t)
    if res != 1:
        t += disks[1][1]
    else:
        break
elapsed_time = time.time() - start_time
print("The answer is ", t - 1, "\n%.3f seconds" % elapsed_time)
