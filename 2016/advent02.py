finput = open("input2.txt", 'r')
keyboard = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
code = []
curRow = 1
curCol = 1
for symbol in finput.read():
    if symbol == 'L':
        if curCol != 0:
            curCol -= 1
    elif symbol == 'R':
        if curCol != 2:
            curCol += 1
    elif symbol == 'D':
        if curRow != 2:
            curRow += 1
    elif symbol == 'U':
        if curRow != 0:
            curRow -= 1
    elif symbol == '\n':
        code.append(keyboard[curRow][curCol])
if symbol != '\n':
    code.append(keyboard[curRow][curCol])
print(code)
finput.close()

finput = open("input2.txt", 'r')
code = []
curRow = 2
curCol = 0
keyboard2 = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
]
for symbol in finput.read():
    if symbol == 'L':
        if curCol != 0 and keyboard2[curRow][curCol-1] != 0:
            curCol -= 1
    elif symbol == 'R':
        if curCol != 4 and keyboard2[curRow][curCol+1] != 0:
            curCol += 1
    elif symbol == 'D':
        if curRow != 4 and keyboard2[curRow+1][curCol] != 0:
            curRow += 1
    elif symbol == 'U':
        if curRow != 0 and keyboard2[curRow-1][curCol] != 0:
            curRow -= 1
    elif symbol == '\n':
        code.append(keyboard2[curRow][curCol])
if symbol != '\n':
    code.append(keyboard2[curRow][curCol])
print(code)
finput.close()
