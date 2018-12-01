import sys
from itertools import combinations
from collections import Counter

res1 = 0
res2 = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        words = line.strip().split(' ')
        if len(set(words)) == len(words):
            res1 += 1
            res2_flag = True
            for s1, s2 in combinations(words, 2):
                c1 = Counter(list(s1))
                c2 = Counter(list(s2))
                if c1 == c2:
                    res2_flag = False
            if res2_flag:
                res2 += 1

print(res1, res2)
