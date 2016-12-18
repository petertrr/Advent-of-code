import time

#task = '..^^.'
#rows = 3
task = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'
#rows = 40
#rows = 400000
rows = 4000

def show_row(row):
    res = ''
    for s in row:
        res += '^' if s else '.'
    print(res)

#def build_row(index):
#

start_time = time.time()
row = [0b1 if s == '^' else 0b0 for s in task]
l = len(row)
counter = row.count(0b0)
#row = task
for i in range(1, rows):
    row = [row[1]] + [row[i-1] ^ row[i+1] for i in range(1, l - 1)] + [row[-2]]
    counter += row.count(0b0)
#    row = [row[1]] + ['^' if (row[i-1] == '.') ^ (row[i+1] == '.') else '.' for i in range(1, len(row) - 1)] + [row[-2]]
elapsed_time = time.time() - start_time
print(counter, " safe tiles")
print("It took %.3f seconds" % elapsed_time)