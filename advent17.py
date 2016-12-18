from hashlib import md5
from collections import deque
import re
import time

#task = 'hijkl'
#task = 'ihgpwlah'
task = 'rrrbmfta'  # my real task
directions = ('U', 'D', 'L', 'R')


class Node:
    def __init__(self, x, y, path='', mark=False, children=[]):
        self.opens = []
        self.path_to_node = path
        self.mark = mark
        self.children = children
        self.x = x
        self.y = y

    def find_possible_directions(self):
        cur = (task + self.path_to_node).encode('utf-8')
        m = md5()
        m.update(cur)
        cur = m.hexdigest()[:4]
        del m
        for i in range(0, 4):
            if re.match('[b-f]', cur[i]):
                self.opens.append(directions[i])

        for o in self.opens:
            if o == 'L' or o == 'R':
                if self.x + self.dx(o) > 4 or self.x + self.dx(o) < 0:
                    self.opens.remove(o)
            elif self.y + self.dy(o) > 4 or self.y + self.dy(o) < 0:
                self.opens.remove(o)


    def generate_children(self):
        for o in self.opens:
            ch = Node(self.x + self.dx(o), self.y + self.dy(o), self.path_to_node + o, False, [])
            self.children.append(ch)
            ch.find_possible_directions()

    def dy(self, dir):
        if dir == 'U':
            return -1
        elif dir == 'D':
            return 1
        else:
            return 0

    def dx(self, dir):
        if dir == 'L':
            return -1
        elif dir == 'R':
            return 1
        else:
            return 0

    def show(self):
        print("Path: ", self.path_to_node)
        print("Open doors: ", self.opens)
        print("Marked as: ", self.mark)
        print("Child nodes: ")
        #for ch in self.children:
        #    ch.show()
        print(self.children)
        print('\n')

start_time = time.time()
root = Node(0, 0)
root.find_possible_directions()
root.generate_children()
print("Root: ", root)
root.show()
for ch in root.children:
    print("child: ", ch)
    ch.show()

Q = deque()
Q.append(root)
length = 0
while len(Q) != 0:
    u = Q.popleft()
    for ch in u.children:
        if ch.mark == False:
#            ch.find_possible_directions()
            ch.generate_children()
            Q.append(ch)
    u.mark = True
    if u.x == 3 and u.y == 3:
#        print(len(u.path_to_node), u.path_to_node)
        if len(u.path_to_node) > length:
            length = len(u.path_to_node)
            print(length)        
        break
    del u
print('The end')
elapsed_time = time.time() - start_time
print("It took %.3f seconds" % elapsed_time)