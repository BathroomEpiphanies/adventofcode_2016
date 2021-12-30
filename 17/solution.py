import sys
from hashlib import md5
import itertools
import collections


passcodes = [l.strip() for l in sys.stdin.readlines()]


Direction = collections.namedtuple('direction',['name','val'])
dirs = [ Direction('U',+0-1j), Direction('D',+0+1j), Direction('L',-1+0j), Direction('R',1+0j) ]
rooms = {r+c*1j for r,c in itertools.product(range(4),repeat=2)}


def find_path(passcode, shortest=True):
    start = 0+0j
    goal = 3+3j
    shortest = None
    longest = None
    queue = collections.deque()
    queue.append( (start,'') )
    visited = set()
    while queue:
        pos,path = queue.popleft()
        if (pos,path) in visited:
            continue
        visited.add((pos,path))
        if pos == goal:
            if not shortest:
                shortest = path
            longest = path
            continue
        for d in [d for d,s in zip(dirs,md5(f'{passcode}{path}'.encode()).hexdigest())
                  if (s in 'bcdef') and (pos+d.val in rooms)]:
            queue.append( (pos+d.val,path+d.name) )
    return shortest,longest


for passcode in passcodes:
    shortest,longest = find_path(passcode)
    print('*1:',shortest)
    print('*2:',len(longest) if longest else float('inf'))
