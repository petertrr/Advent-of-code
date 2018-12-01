import re

ROWS = 6
COLUMNS = 50
instructions = open('advent8.txt', 'r')


def render(matrix):
    for row in matrix:
        ren_row = ''
        for s in row:
            if s:
                ren_row += '#'
            else:
                ren_row += '.'
        print(ren_row)
    print('\n')


def rect(matrix, A, B):
    for i in range(0, B):
        for j in range(0, A):
            matrix[i][j] = True


def rotate(matrix, flag, A, B):
    if flag:
        temp = [matrix[i][A] for i in range(0, ROWS)]
        for i in range(0, ROWS):
            matrix[(i + B) % ROWS][A] = temp[i]
    else:
        temp = [matrix[A][j] for j in range(0, COLUMNS)]
        for j in range(0, COLUMNS):
            matrix[A][(j + B) % COLUMNS] = temp[j]


def count_lit(matrix):
    count = 0
    for row in matrix:
        for s in row:
            if s:
                count += 1
    return count

matrix = [[False for j in range(0, COLUMNS)] for i in range(0, ROWS)]
render(matrix)
while True:
    line = instructions.readline()
    if len(line) == 0:
        break
    command = re.findall(r'\w+', line)
    args = re.findall(r'\d+', line)
    print(command[0], args)
    if command[0] == 'rect':
        rect(matrix, int(args[0]), int(args[1]))
    elif command[0] == 'rotate':
        if command[1] == 'column':
            rotate(matrix, True, int(args[0]), int(args[1]))
        elif command[1] == 'row':
            rotate(matrix, False, int(args[0]), int(args[1]))
    render(matrix)
print(count_lit(matrix))