import sys

with open(sys.argv[1], 'r') as f:
    seq = list(map(int, ''.join(f.readlines()).strip()))

l = len(seq)
res1 = sum(s for i, s in enumerate(seq) if s == seq[(i+1) % l])
res2 = sum(s for i, s in enumerate(seq) if seq[i] == seq[(i + l // 2) % l])
print(res1, res2)

