import sys
import itertools

program = [l.strip().split() for l in sys.stdin.readlines()]

b = int(program[1][1])
c = int(program[2][1])
d = b*c

n = 1
p = 0
while n<d:
    n = n*2+p
    p = 1-p
a = n-d

print('*1:',a)
