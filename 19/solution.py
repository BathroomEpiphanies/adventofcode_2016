import sys
import collections


number = int(sys.stdin.readlines()[0])


elves = collections.deque(range(1,number+1))
while elves:
    elves.rotate(-1)
    winner = elves.popleft()
print('*1:',winner)


elves = collections.deque(range(1,number+1))
elves.rotate(-(number//2))
while elves:
    winner = elves.popleft()
    elves.rotate(-((len(elves)+1)%2))
print('*2:',winner)
