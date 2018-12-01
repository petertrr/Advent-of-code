import re


def parse(code):
    pattern = r'^(\w*)(?:(\(\d+x\d+\))(.*))*'
    partsL = re.findall(pattern, code)
    parts = partsL[0]
    result = parts[0]
    if len(parts[1]) != 0:
        s = parts[1]
        num1 = int(s[1:s.index('x')])
        num2 = int(s[s.index('x') + 1:-1])
        result += parts[2][0:num1] * num2 + parse(parts[2][num1:])
    return result


def decompressed_length(code):
    pattern = r'^(\w*)(?:(\(\d+x\d+\))(.*))*'
    partsL = re.findall(pattern, code)
    parts = partsL[0]
    result = len(parts[0])
    if len(parts[1]) != 0:
        s = parts[1]
        num1 = int(s[1:s.index('x')])  # first value from command
        num2 = int(s[s.index('x') + 1:-1])  # second value
        result += decompressed_length(parts[2][0:num1]) * num2 + decompressed_length(parts[2][num1:])
    return result

task = open("advent9.txt", 'r')
answer = 0
while True:
    line = task.readline()
    if len(line) == 0:
        break
    decipher = parse(line)
    answer += len(decipher)
print(answer)
task.close()

task = open("advent9.txt", 'r')
while True:
    line = task.readline()
    if len(line) == 0:
        break
    answer = decompressed_length(line)
print(answer)
