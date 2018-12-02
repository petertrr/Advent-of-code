from collections import Counter
from itertools import combinations, chain

with open("02.input") as f:
    ids = [l.strip() for l in f.readlines() if l.strip()]

res = Counter(chain.from_iterable(
         set(v for v in Counter(id).values() if v in (2, 3)) for id in ids))
print("{} * {} = {}".format(res[2], res[3], res[2] * res[3]))

for pair in combinations(ids, 2):
    diff = list(filter(lambda c: c[0] != c[1], zip(pair[0], pair[1])))
    if len(diff) == 1:
        print(pair, diff)
        break
