import sys
from itertools import combinations

res1, res2 = 0, 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        arr = list(sorted(map(int, line.strip().split())))
        res1 += arr[-1] - arr[0]
        for p1, p2 in combinations(arr, 2):
            if p2 % p1 == 0:
                res2 += p2 // p1
                break

print(res1, res2)
