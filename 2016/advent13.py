import matplotlib.pyplot as plt
import numpy as np

number = 1350
size_x = 70
size_y = 70
aim_x = 31
aim_y = 39

image = np.zeros(size_y*size_x)

def sum_digits(num, base=10):
    r = 0
    while num:
        r, num = r + num % base, num // base
    return r


def show_maze():
    for j in range(0, size_y):
        row = ''
        for i in range(0, size_x):
            if maze[j][i][0] == None:
                row += '?'
            elif maze[j][i][0]:
                row += '.'
            else:
                row += '#'
        print(row)
    print('\n')
    for j in range(0, size_y):
        row = ''
        for i in range(0, size_x):
            if maze[j][i][0] == None:
                row += '?'
            elif maze[j][i][0]:
                row += str(maze[j][i][1])
            else:
                row += '#'
        print(row)


def steps(x, y):
    arr = []
    for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y -1)]:
        if 0 <= nx < size_x and 0 <= ny < size_y and maze[ny][nx][0] and (maze[ny][nx][1] == -1 or maze[ny][nx][1] > maze[y][x][1] + 1):
            maze[ny][nx][1] = maze[y][x][1] + 1
            steps(nx, ny)

maze = [
    [[None, -1] for i in range(0, size_x)]
    for j in range(0, size_y)
]
for i in range(0, size_x):
    for j in range(0, size_y):
        if (sum_digits(i * i + 3 * i + 2 * i * j + j + j * j + number, 2) % 2) == 0:
            maze[j][i][0] = True
        else:
            maze[j][i][0] = False

maze[1][1][1] = 0
steps(1, 1)
#show_maze()
print(maze[aim_y][aim_x][1])
count = 0
for i in range(0, size_x):
    for j in range(0, size_y):
        if maze[j][i][1] != -1 and maze[j][i][1] <= 50:
            count += 1
print(count)

data = [[0 for i in range(0, size_x)] for j in range(0, size_y)]
#data = [[maze[j][i][1] for i in range(0, size_x)] for j in range(0, size_y)]
for j in range(0, size_y):
    for i in range(0, size_x):
        if maze[j][i][0]:
            data[j][i] = maze[j][i][1]
        else:
            data[j][i] = 0
walls = [[0 for i in range(0, size_x)] for j in range(0, size_y)]
walls_x = []
walls_y = []
for j in range(0, size_y):
    for i in range(0, size_x):
        if not maze[j][i][0]:
            walls_x.append(i)
            walls_y.append(j)
#for j in range(0, size_y):
#    for i, (image_row, data_row) in enumerate(zip(image, data[j])):
#        image_row[i % 2::2] = data_row
#plt.matshow(image)
x = [i for i in range(0, 10)]
y = [i**2 for i in range(0, 10)]
#plt.plot(x, y)
plt.imshow(data, interpolation='nearest')
#plt.imshow(walls, interpolation='nearest')
plt.show()
