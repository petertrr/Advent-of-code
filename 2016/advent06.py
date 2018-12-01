input = open("advent6.txt", 'r')
STR_LEN = 8
letters = [{} for i in range(0, STR_LEN)]
decipher = ['', '']
lines = 0
while True:
    line = input.readline()
    if len(line) == 0:
        break
    lines += 1
    for i in range(0, STR_LEN):
        s = line[i]
        if s not in letters[i]:
            letters[i].update({s: 1})
        elif s != '\n':
            letters[i][s] += 1
for i in range(0, STR_LEN):
    max = 0
    min = lines
    symbol_max = ''
    symbol_min = ''
    for s in letters[i]:
        if letters[i][s] > max:
            max = letters[i][s]
            symbol_max = s
        if letters[i][s] < min:
            min = letters[i][s]
            symbol_min = s
    decipher[0] += symbol_max
    decipher[1] += symbol_min
print(decipher)
