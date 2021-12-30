import sys
import collections


lines = [l.strip() for l in sys.stdin.readlines()]
number = int(lines[0])
goal = [int(n) for n in lines[1].split(',')]
goal = goal[0]+goal[1]*1j


dirs = [ +1+0j, +0+1j, -1+0j, +0-1j ]

def is_wall(p):
    if p.real<0 or p.imag<0:
        return 1
    else:
        return f'{int(p.real**2 + 3*p.real + 2*p.real*p.imag + p.imag + p.imag**2 + number):b}'.count('1')%2

for y in range(50):
    for x in range(50):
        if x+y*1j == 1+1j:
            print('S',end='')
        elif x+y*1j == goal:
            print('G',end='')
        else:
            print('#' if is_wall(x+y*1j) else '.',end='')
    print()


start = (1+1j)
queue = collections.deque()
queue.append((0,start))
visited = set()
shortest = None
reachable = None
while queue:
    dist,pos = queue.popleft()
    if not shortest and pos==goal:
        shortest = dist
    if not reachable and dist>50:
        reachable = len(visited)
    if shortest and reachable:
        break
    if pos in visited:
        continue
    visited.add(pos)
    for d in dirs:
        if not is_wall(pos+d):
            queue.append((dist+1,pos+d))
            
print('*1:', shortest)
print('*2:', reachable)
