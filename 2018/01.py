#!/env/python3

from collections import Counter  # using Counter allows to catch frequency occuring more than once
from itertools import accumulate, cycle

N = 2  # number of times frequency is required
frequencies = Counter()
with open("01.input") as f:
    df = [int(l) for l in f.readlines() if l.strip()]
freq_2 = next(f for f in accumulate(cycle(df)) if frequencies[f] == N - 1 or frequencies.update((f,)))

print("Final frequency is {}".format(sum(df)))
print("First frequency to be reached twice: {}".format(freq_2))
