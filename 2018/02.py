from collections import Counter
from itertools import combinations

with open("02.input") as f:
    ids = [l.strip() for l in f.readlines() if l.strip()]

ids_with_2 = 0
ids_with_3 = 0

for id in ids:
    c = Counter(Counter(id).values())
    ids_with_2 += 1 if c[2] > 0 else 0
    ids_with_3 += 1 if c[3] > 0 else 0

print("{} * {} = {}".format(ids_with_2, ids_with_3, ids_with_2 * ids_with_3))

for pair in combinations(ids, 2):
    l = list(filter(lambda c: c[0] != c[1], zip(pair[0], pair[1])))
    if len(l) == 1:
        print(pair, l)
        break
