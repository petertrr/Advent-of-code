import time

#pylint: disable=C0103

start_time = time.time()
#number_of_elves = 5
number_of_elves = 3004953
elves = [[i, 1] for i in range(1, number_of_elves + 1)]


def direct_simulation():
    i = 0
    while len(elves) != 1:
        cur_len = len(elves)
        if elves[i % cur_len][1] != 0:
            elves[i % cur_len][1] += elves[(i+1) % cur_len][1]
            elves.pop((i+1) % cur_len)
    #        print(elves)
        else:
            elves.pop(i % cur_len)
        i = (i + 1) % cur_len
    print(elves)            



    elves = [i for i in range(1, number_of_elves + 1)]
    i = 0
    while len(elves) != 1:
        cur_len = len(elves)
        elves.pop((i+1)%cur_len)
        i = (i+1) % (cur_len)
    print(elves)

def func(n):
    elves = [i for i in range(1, n, 2)] if n % 2 == 0 else [n] + [i for i in range(1, n, 2)]
#    print(elves)
    i = 0
    while len(elves) != 1:
        cur_len = len(elves)
        elves.pop((i+1)%cur_len)
        i = (i+1) % (cur_len)
#        print(elves)
    return elves[0]


def idea(n, s, i, n0):
    if n == 2:
        return s
    elif n == 3:
        return (s + i) % (n0 - 1)
    else:
        return idea(n/2 + n % 2, (n - 1 + n0 % 2) % n0, i * 2, n0)


def iterate(circle):
    length = len(circle)
    if length % 2 == 0:
        return [circle[i] for i in range(0, length, 2)]
    else:
        return [circle[-1]] + [circle[i] for i in range(0, length - 1, 2)]


def solve(n):
    #elves = [i for i in range(1, n + 1)]
    elves = [i for i in range(1, n, 2)] if n % 2 == 0 else [n] + [i for i in range(1, n, 2)]
    while len(elves) != 1:
        elves = iterate(elves)
    return elves

#direct_simulation()
#fast_method()
#cycle()
#func(number_of_elves)
#print(idea(number_of_elves, 0, 0, number_of_elves) + 1)
#for i in range(2, 10):
#    print(i, ": ", func(i), " vs ", idea(i, 0, 1, i) + 1)
print(solve(number_of_elves))
elapsed_time = time.time() - start_time
print("Took %.3f seconds" % elapsed_time)
