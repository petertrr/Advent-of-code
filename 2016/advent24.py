task = open("advent24.txt", 'r')
maze = []
while True:
    row = task.readline()
    if len(row) == 0:
        break
    maze.append(row[:-1])
print(maze)
