import re
from itertools import chain
from functools import reduce


class Claim:
    pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'

    def __init__(self, claim_str):
        arr = re.findall(self.pattern, claim_str)[0]
        self.id = int(arr[0])
        self.margin_x = int(arr[1])
        self.margin_y = int(arr[2])
        self.width_x = int(arr[3])
        self.width_y = int(arr[4])


task = open("03.input").readlines()

claims = set(Claim(line.strip()) for line in task)

x_max = max(c.margin_x + c.width_x for c in claims)
y_max = max(c.margin_y + c.width_y for c in claims)

fabric = [[0 for _ in range(y_max)] for _ in range(x_max)]

overlaps = {c.id: False for c in claims}
overlaps.update({-1: True})

for c in claims:
    for i in range(c.margin_x, c.margin_x + c.width_x):
        for j in range(c.margin_y, c.margin_y + c.width_y):
            if fabric[i][j] == 0:
                fabric[i][j] = c.id
            elif fabric[i][j] != 0:
                overlaps[fabric[i][j]] = True
                overlaps[c.id] = True
                fabric[i][j] = -1

print(reduce(lambda count, i: count + (1 if i < 0 else 0), chain(*fabric)))
print(next(c for c in overlaps if not overlaps[c]))
