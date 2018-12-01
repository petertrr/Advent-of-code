import sys
import numpy as np

with open(sys.argv[1]) as f:
    arr = list(map(lambda s : int(s.strip()), f.readlines()))

arr1 = arr[:]
i = 0
res1 = 0
while i < len(arr):
    res1 += 1
    arr[i] += 1
    i += arr[i] - 1

i = 0
res2 = 0
while i < len(arr1):
    res2 += 1
    modif = 1 if arr1[i] < 3 else -1
    arr1[i] += modif
    i += arr1[i] - modif
print(res1, res2)
