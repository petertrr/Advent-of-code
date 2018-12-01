# collecting code
task = open('advent12.txt', 'r')
instructions = []
while True:
    line = task.readline()
    if len(line) == 0:
        break
    if line.find('\n') != -1:
        line = line[:-1]
    instructions.append(line)
task.close()


def show_register():
    print('a\tb\tc\td')
    print('%d\t%d\t%d\t%d' % (a, b, c, d))
    print('\n')

def transofrm(instructions, line1, line2):
    position = line1
    code = ''
    block_pos = []
    while position < line2:
        commands = instructions[position].split(' ')
    #    print(position, commands)
        if commands[0] == 'cpy':
            code += '%s = %s\n' % (commands[2], commands[1])
        elif commands[0] == 'inc':
            code += '%s += 1\n' % commands[1]
        elif commands[0] == 'dec':
            code += '%s -= 1\n' % commands[1]
        elif commands[0] == 'jnz':
            block_pos.append(position + int(commands[2]))
            code += 'if %s != 0:goto .label%d\n' % (commands[1], len(block_pos))
        position += 1
    return (code, block_pos)

def perform1():
    position = 0
    while position < len(instructions):
        commands = instructions[position].split(' ')
    #    print(position, commands)
        if commands[0] == 'cpy':
            if commands[1] in vars():
                vars()[commands[2]] = vars()[commands[1]]
            else:
                vars()[commands[2]] = int(commands[1])
            position += 1
        elif commands[0] == 'inc':
            vars()[commands[1]] += 1
            position += 1
        elif commands[0] == 'dec':
            vars()[commands[1]] -= 1
            position += 1
        elif commands[0] == 'jnz':
            if commands[1] in vars():
                if vars()[commands[1]] != 0:
                    position += int(commands[2])
                else:
                    position += 1
            else:
                if int(commands[1]) != 0:
                    position += int(commands[2]) * int(commands[1]) // abs(int(commands[1]))

#pefrorming instructions
# initializing registers
a = 0
b = 0
c = 0
d = 0
#perform1()


code, block_pos = transofrm(instructions, 0, len(instructions))
lines = code.split('\n')
code = ''
j = 1
print(block_pos)
for i in range(0, len(lines)):
    while i in block_pos:
        code += 'label .label' + str(block_pos.index(i) + 1)
        block_pos.pop(block_pos.index(i))
        j += 1
    code += lines[i] + '\n\t'

code = code.replace(':', ':\n\t\t')
#for i in range(1, len(block_pos) + 1):
i = 0
while i <= len(block_pos):
    code = code.replace('label .label%s' % i, 'label .label%s\n\t' % i)
    i += 1
code = 'from goto import with_goto\n\na = 0\nb = 0\nc = 0\nd = 0\n\n\n@with_goto\ndef code(a, b, c, d):\n\t' \
       + code + 'print(a, b, c, d)\n\treturn (a, b, c, d)\ncode(a, b, c, d)'
#print(code)
output = open('advent12_py.py', 'w')
output.write(code)
#import advent12_py
#print(advent12_py.code(a, b, c, d))
exec(compile(open('advent12_py.py', "rb").read(), 'advent12_py.py', 'exec'))
show_register()
