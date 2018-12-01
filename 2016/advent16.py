# using generator to create reversed string in spite of symbol-by-symbol parsing decreased time from 60 s to 36 s
# using list in spite of strings, while calculating checksum, decreased time from 36 s to 15 s
# using zipped pair and range-based cycle in checksum in spite of while cycle decreased from 15 s to 9 s
# first attempt to optimize algorithm by not generating full string achieved 7 s.
# Because there are only 17 still enormous chunks

import time
#disk_space = 272
disk_space = 35651584
task = '01111001100111011'


def gen_step(data):
    data_rev = ''.join('0' if s == '1' else '1' for s in reversed(data))
    return '{}0{}'.format(data, data_rev)


def generate(data, limit):
    while len(data) < limit:
        data = gen_step(data)
    return data[:limit]


def checksum(a):
    res = []
    for a, b in zip(a[::2], a[1::2]):
        if a == b:
            res.append('1')
        else:
            res.append('0')
    if len(res) % 2 != 0:
        return ''.join(res)
    else:
        return checksum(res)


def quick_function(a):
    a_rev = ''.join('0' if s == '1' else '1' for s in reversed(a))
    chunks_num = disk_space
    steps = 0
    n = 0
    while chunks_num % 2 == 0:
        chunks_num //= 2
        steps += 1
        n = 2 * n + 1
    separators = generate('0', n)
    print('n = ', n, ', length = ', chunks_num, ', steps = ', steps, ", chunk size = ", 2**steps)
    chunk_size = 2**steps
    chunks = disk_space / chunk_size
    fragment = ''
#    fragment_len = 0
    sum = ''
    i = 0
    j = 0
    while j < chunks:
        if len(fragment) > chunk_size:
#        if fragment_len > chunk_size:
            fragment = fragment[chunk_size:] + separators[i]
#            fragment_len +=
#            separators = separators.replace(separators[0], '')
            i += 1
        else:
            fragment = ''
        while len(fragment) < chunk_size:
            fragment += a if i % 2 == 0 else a_rev
            if len(fragment) >= chunk_size:
                break
            fragment += separators[i]
            i += 1
#            separators = separators.replace(separators[0], '')
            if len(fragment) >= chunk_size:
                break
        temp = 0
        for s in fragment[:chunk_size]:
            temp += 1 if s == '1' else 0
        sum += '1' if temp % 2 == 0 else '0'
        j += 1
    return sum

# sketch of optimization
#    data_len = len(a)
#    while i < n:
#        temp = 0
#        j = 0
#        flag = 0
#        while j < chunk_size and i < n:
#            if i % 2 == 0:
#                for s in a:
#                    temp += 1 if s == '1' else 0
#                    j += 1
#                    if j > chunk_size:
#                        break
#            else:
#                for s in a_rev:
#                    temp += 1 if s == '1' else 0
#                    j += 1
#                    if j > chunk_size:
#                        break
#            if j > chunk_size:
#                break
#            temp += 1 if separators[i] == '1' else 0
#            i += 1
#            j += 1
#        sum += '1' if temp % 2 == 0 else '0'
#    return sum


start_time = time.time()
#sum = checksum(generate(task, disk_space))
sum = quick_function(task)
elapsed_time = time.time() - start_time
print("Sum is ", sum, ". Calculation took %f seconds" % elapsed_time)
