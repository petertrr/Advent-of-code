import time

#task = '..^^.'
#rows = 3
task = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'
room = [
    task,
    ]
#rows = 40
#rows = 400000
rows = 4000

def show():
    for i in range(0, rows - 1):
        room.append(new_row(room[-1]))
    for r in room:
        print(r)
    counter = 0
    for s in room:
        for ch in s:
            if ch == '.':
                counter += 1
    elapsed_time = time.time() - start_time
    print(counter, " safe tiles")

def new_row(row):
    new_row = '^' if row[1] == '^' else '.'
    for i in range(1, len(row) - 1):
        if (row[i - 1] == '^' and row[i + 1] != '^') or (row[i + 1] == '^' and row[i - 1] != '^'):
            new_row += '^'
        else:
            new_row += '.' 
    new_row += '^' if row[-2] == '^' else '.'
    return new_row

start_time = time.time()
#show()
counter = 0
row = task
for i in range(0, rows):
    for ch in row:
        if ch == '.':
            counter += 1
    row = new_row(row)
elapsed_time = time.time() - start_time
print(counter, " safe tiles")
print("It took %.3f seconds" % elapsed_time)