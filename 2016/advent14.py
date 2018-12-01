from hashlib import md5
import re
import time

hashes = {}
def mem_md5(code):
    if code not in hashes:
        m = md5()
        m.update(code)
        code_hash = m.hexdigest()
        del m
        hashes.update({code: code_hash})
    return hashes[code]

start_time = time.time()
test = 'abc'
real = 'qzyelonm'
task = real
indexes = []
i = 0 # > 342 
index1 = {}
index2 = -1
#num = []
while len(indexes) < 64:
    cur = task + str(i)
    cur = cur.encode('utf-8')
    for j in range(0, 1):
#        cur = mem_md5(cur)
        m = md5()
        m.update(cur)
        cur = m.hexdigest()
        del m
    hash = cur
#    print(hash)
#    if num[-1] == -1:
    rep = re.findall(r'(.)\1{2,}', hash)
    if len(rep) != 0:
        index1.update({i: rep[0]})
#        num.append(rep[0])
#        index1.append(i)
#        print(index1, num, hash)
    for index in index1:
        rep = re.findall('(%s){5}' % index1[index], hash)
        if len(rep) != 0:
            index2 = i
#            print(index2, num, hash)
            indexes.append(i)
            print(len(indexes), ': ', indexes[-1])
            index1.pop(index)
            break
#            num = -1
#            i = indexes[-1]
    if len(indexes) > 0 and i > min(index1.keys()) + 1000:
        index1.pop(min(index1.keys()))
#        i = index1
  #  break
    i += 1
elapsed_time = time.time() - start_time
print("It's taken %.3f seconds" % elapsed_time)
