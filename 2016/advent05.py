from hashlib import md5
import re
import time


def first_decipher(input):
    output = ''
    end = False
    i = 0
    while not end:
        cur = input + str(i)
        cur = cur.encode('utf-8')
    #    print(cur)
        m = md5()
        m.update(cur)
        hash = m.hexdigest()
    #    print(hash)
        if re.match('00000[\d]*', hash):
            output += hash[5]
        i += 1
        del m
        if len(output) == 8:
            end = True
    return output


def second_decipher(input):
    output = ''
    end = False
    i = 0
    keys = {}
    while not end:
        cur = input + str(i)
        cur = cur.encode('utf-8')
    #    print(cur)
        m = md5()
        m.update(cur)
        hash = m.hexdigest()
    #    print(hash)
        if re.match('00000[0-7][\d]*', hash) and int(hash[5]) not in keys:
            keys.update({int(hash[5]): hash[6]})
    #       print(hash[5], hash[6], i, hash)
        i += 1
        del m
        if len(keys) == 8:
            end = True
    #print(keys)
    for i in range(0, 8):
        output += keys[i]
    return output

start_time = time.time()
test_task = 'abc'
task = 'ugkcyxxp'
#print('password #1 is ' + first_decipher(task))
print('password #2 is ' + second_decipher(task))
elapsed_time = time.time() - start_time
print("I've spent %.3f seconds" % elapsed_time)