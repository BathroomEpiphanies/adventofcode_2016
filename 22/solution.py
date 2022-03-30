import sys
import re
import collections
import itertools
import json
import numpy as np


Node = collections.namedtuple('Node',['size','used'])

lines = [l.strip() for l in sys.stdin.readlines()]


maxx = 0
maxy = 0
nodes = {}
empty = None
for line in lines[2:]:
    m = re.match(r'/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%', line)
    x,y = int(m.group(1)),int(m.group(2))
    size,used = int(m.group(3)),int(m.group(4))
    maxx,maxy = max(maxx,x),max(maxy,y)
    if used==0:
        empty = (x,y)
    nodes[(x,y)] = Node(size,used)


def print_nodes():
    for y in range(maxy+1):
        for x in range(maxx+1):
            print(f'({nodes[(x,y)].used:3d}/{nodes[(x,y)].size:3d})', end='  ')
        print()

viable = 0
for a,b in itertools.permutations(nodes,2):
    if nodes[b].used > 0 and nodes[b].used <= nodes[a].size-nodes[a].used:
        viable += 1

#print_nodes()

print('*1:',viable)
# empty node needs to be moved all the way around, then it takes 5 moves to rotate target node 1 location closer to the goal
print('*2:',maxx+sum(empty)+5*(maxx-1))
