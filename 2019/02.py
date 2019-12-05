def parse_registry(r):
    idx = 0
    while True:
        if r[idx] == 1:
            r[r[idx+3]] = r[r[idx+1]] + r[r[idx+2]]
            idx += 4
        elif r[idx] == 2:
            r[r[idx+3]] = r[r[idx+1]] * r[r[idx+2]]
            idx += 4
        elif r[idx] == 99:
            return


with open('02.input') as f:
    registry = [int(n) for n in f.readline().strip().split(',')]
init_mem = [r for r in registry]

# part 1
registry[1] = 12
registry[2] = 2
parse_registry(registry)
print(registry[0])

# part 2
goal = 19690720
for i in range(0, 100):
    for j in range(0, 100):
        registry = [r for r in init_mem]
        registry[1] = i
        registry[2] = j
        parse_registry(registry)
        if registry[0] == goal:
            print(f"{i}, {j}, {registry[0]}")
