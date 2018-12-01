import sys

res1 = 0
count = 0
with open(sys.argv[1], 'r') as f:
    while True:
        c = f.read(1)
        if count is not None:
            count += 1
        if not c:
            break
        if c == '(':
            res1 += 1
        elif c == ')':
            res1 -= 1
        if res1 == -1 and count is not None:
            print("Count: ", count)
            count = None

print(res1)
