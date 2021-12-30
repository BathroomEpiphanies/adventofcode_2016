import sys


directions = [(d[0],int(d[1:])) for d in sys.stdin.readlines()[0].split(', ')]

position = 0+0*1j
heading = 0+1*1j
visited = {position}
first_twice = None
for turn,steps in directions:
    heading *= {'L':1j, 'R':-1j}[turn]
    for i in range(steps):
        position += heading
        if first_twice is None and position in visited:
            first_twice = position
        visited.add(position)
        

print('*1:', int(abs(position.real)+abs(position.imag)))
print('*2:', int(abs(first_twice.real)+abs(first_twice.imag)))
