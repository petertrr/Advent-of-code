from math import ceil, sqrt

task = 289326


def find_distance(number):
    print("For number = {}".format(number))
    n = ceil((sqrt(number) - 1) / 2)
    start = 2 + 4 * n * (n - 1)
    n_elems = 8 * n
    len_row = n_elems // 4
    idx = (number - start) % len_row
    print(n + abs(len_row // 2 - 1 - idx))


find_distance(task)
