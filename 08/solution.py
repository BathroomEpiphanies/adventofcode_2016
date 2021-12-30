import sys
import numpy as np
np.set_printoptions(edgeitems=50, linewidth=180)


lines = [l.strip() for l in sys.stdin.readlines()]


display = np.zeros((6,50),'uint8')

for line in lines:
    operation,remainder = line.split(' ',1)
    if operation == 'rect':
        w,h = (int(n) for n in remainder.split('x'))
        display[:h,:w] = 1
    elif operation == 'rotate':
        direction,remainder = remainder.split('=',1)
        if direction == 'column x':
            column,shift = (int(n) for n in remainder.split(' by '))
            display[:,column] = np.roll(display[:,column],shift)
        elif direction == 'row y':
            row,shift = (int(n) for n in remainder.split(' by '))
            display[row,:] = np.roll(display[row,:],shift)

print('*1:',display.sum())
print('*2:')
print('\n'.join([''.join('#' if c else ' ' for c in r) for r in display]))


