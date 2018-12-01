import re
import time

nodes = {}
task = open('advent22.txt', 'r')
start_time = time.time()
while True:
    line = task.readline()
    if len(line) == 0:
        break
    nums = re.findall(r'(\d+)', line)
    if len(nums) != 0:
        nodes.update({(int(nums[0]), int(nums[1])): {'size': int(nums[2]), 'used': int(nums[3]), 'avail': int(nums[4])}})
pairs = 0
avail = list(reversed(list(nodes.keys())))
for n in nodes:
    i = 0
    for m in nodes:
        if 0 < nodes[n]['used'] <= nodes[m]['avail'] and not (m[0] == n[0] and n[1] == m[1]):
            pairs += 1
        i += 1
print(pairs)
elapsed_time = time.time() - start_time
print("It took {0:.3f} seconds".format(elapsed_time))