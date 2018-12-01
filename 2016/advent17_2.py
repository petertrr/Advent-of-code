from hashlib import md5
from collections import deque
from itertools import compress
import time

#pylint: disable=C0103

#task = 'hijkl'  # no way through maze
#task = 'ihgpwlah'  # p.1: DDRRRD, p.2: 370
#task = 'kglvqrro'  # p.1: DDUDRLRRUDRD, p.2: 492
task = 'ulqzkmiv'  # p.1: DRURDRUDDLLDLUURRDULRLDUUDDDRR, p.2: 830
#task = 'rrrbmfta'  # my real task
directions = ('U', 'D', 'L', 'R')

cur_level = deque()
next_level = deque()

moves = {
    'U': lambda x, y: (x, y - 1),
    'D': lambda x, y: (x, y + 1),
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y)
     }

class Node:
    def __init__(self, x, y, path=''):
        self.opens = []
        self.path_to_node = path
        self.x = x
        self.y = y

    def find_possible_directions(self):
        cur = (task + self.path_to_node).encode('utf-8')
       # self.opens = compress('UDLR', (int(s, 16) > 10 for s in md5(cur).hexdigest()[:4]))
        cur = md5(cur).hexdigest()[:4]
        for i in range(0, 4):
            if int(cur[i], 16) > 10:
                self.opens.append(directions[i])

    def generate_children(self):
        for o in self.opens:
            nx, ny = moves[o](self.x, self.y)
            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            ch = Node(nx, ny, self.path_to_node + o)
            ch.find_possible_directions()
            next_level.append(ch)

start_time = time.time()
root = Node(0, 0)
root.find_possible_directions()
cur_level.append(root)
length = 0
end = False
while len(cur_level) != 0 and not end:
    while len(cur_level) != 0:
        u = cur_level.popleft()
        if u.x == 3 and u.y == 3:
            if len(u.path_to_node) > length:
                length = len(u.path_to_node)
#                print(length)        
#            end = True
#            break
        else:
            u.generate_children()
    cur_level = next_level
    next_level = deque()
print(length)
print('The end')
elapsed_time = time.time() - start_time
print("It took %.3f seconds" % elapsed_time)