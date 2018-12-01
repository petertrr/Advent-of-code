import sys

res1 = 0
res2 = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        l, w, h = map(int, line.split('x'))
        sides = (l*w, w*h, l*h)
        perims = (2 * (l+w), 2 * (l+h), 2 * (w+h))
        res1 += 2 * sum(sides) + min(sides)
        res2 += min(perims) + l * w * h
print(res1, res2)
