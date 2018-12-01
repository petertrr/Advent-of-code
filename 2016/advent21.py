import time
passwd = 'abcdefgh'
passwd2 = 'fbgdceah'


def scramble(word):
    task = open('advent21.txt', 'r')
    while True:
        line = task.readline().rstrip('\n')
        if len(line) == 0:
            break
        line = line.split(' ')
        if line[0] == 'swap':
            if line[1] == 'position':
                x, y = min(int(line[2]), int(line[5])), max(int(line[2]), int(line[5]))
            elif line[1] == 'letter':
                x, y = min(word.find(line[2]), word.find(line[5])), max(word.find(line[2]), word.find(line[5]))
            word = word[:x] + word[y] + word[x + 1:y] + word[x] + word[y + 1:]
        elif line[0] == 'rotate':
            if line[1] == 'left' or line[1] == 'right':
                steps = -int(line[2]) if line[1] == 'right' else int(line[2])
            elif line[1] == 'based':
                steps = - 1 - word.find(line[-1]) if word.find(line[-1]) < 4 else - 2 - word.find(line[-1])
            buf = ''
            for i in range(0, len(word)):
                buf += word[(i + steps) % len(word)]
            word = buf
        elif line[0] == 'reverse':
            x, y = int(line[2]), int(line[4])
            buf = word[x:y+1]
            word = word[:x] + buf[::-1] + word[y+1:]
        elif line[0] == 'move':
            x, y = int(line[2]), int(line[5])
            buf = word[x]
            word = word[:x] + word[x + 1:]
            word = word[:y] + buf + word[y:]
    task.close()
    return word


def descramble(word):
    task = open('advent21.txt', 'r')
    instructions = task.readlines()
    while True:
        if len(instructions) > 0:
            line = instructions[-1].rstrip('\n')
        else:
            break
        line = line.split(' ')
        if line[0] == 'swap':
            if line[1] == 'position':
                x, y = min(int(line[2]), int(line[5])), max(int(line[2]), int(line[5]))
            elif line[1] == 'letter':
                x, y = min(word.find(line[2]), word.find(line[5])), max(word.find(line[2]), word.find(line[5]))
            word = word[:x] + word[y] + word[x + 1:y] + word[x] + word[y + 1:]
        elif line[0] == 'rotate':
            if line[1] == 'left' or line[1] == 'right':
                steps = int(line[2]) if line[1] == 'right' else -int(line[2])
                buf = ''
                for i in range(0, len(word)):
                    buf += word[(i + steps) % len(word)]
                word = buf
            elif line[1] == 'based':
                i = 0
                ad = 1 if word.index(line[-1]) < 4 else 2
                while word.index(line[-1]) + ad != i:
                    buf = ''
                    for j in range(0, len(word)):
                        buf += word[(j + 1) % len(word)]
                    word = buf
                    ad = 1 if word.index(line[-1]) < 4 else 2
                    i += 1
        elif line[0] == 'reverse':
            x, y = int(line[2]), int(line[4])
            buf = word[x:y+1]
            word = word[:x] + buf[::-1] + word[y+1:]
        elif line[0] == 'move':
            x, y = int(line[2]), int(line[5])
            buf = word[y]
            word = word[:y] + word[y + 1:]
            word = word[:x] + buf + word[x:]
        instructions.pop()
    task.close()
    return word

start_time = time.time()
print("{!r} becomes {!r} after scrambling".format(passwd, scramble(passwd)))
print("{!r} was {!r} before scrambling".format(passwd2, descramble(passwd2)))
elapsed_time = time.time() - start_time
print("It took {0:.1f} miliseconds".format(1000*elapsed_time))