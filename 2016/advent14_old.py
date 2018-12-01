from hashlib import md5
import re
import time


def hash_calc(obj, lim):
    mm = md5()
    mm.update(obj)
    obj = mm.hexdigest()
    del mm
    for i in range(1, lim):
        obj = obj.encode('utf-8')
        mm = md5()
        mm.update(obj)
        obj = mm.hexdigest()
        del mm
    return obj

cycles = 1
start_time = time.time()
test = 'abc'
real = 'qzyelonm'
task = real
indexes = []
i = 0
index1 = -1
index2 = -1
num = -1
while len(indexes) < 64:
    cur = task + str(i)
    cur = cur.encode('utf-8')
    hash = hash_calc(cur, cycles)
    rep = re.findall(r'(.)\1{2}', hash)
    if len(rep) != 0:
        index1 = i
        num = rep[0]
        i += 1
        while i < index1 + 1000:
            cur = task + str(i)
            cur = cur.encode('utf-8')
            hash = hash_calc(cur, cycles)
            rep = re.findall('(%s){5}' % num, hash)
            if len(rep) != 0:
                index2 = i
    #            print(index2, num, hash)
                indexes.append(index1)
                print(len(indexes), ': ', indexes[-1], index2)
                num = -1
                i = indexes[-1]
                break
            i += 1
        i = index1
    i += 1
elapsed_time = time.time() - start_time
print("It's taken %.3f seconds" % elapsed_time)
