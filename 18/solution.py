import sys
import numpy as np
np.set_printoptions(edgeitems=100, linewidth=240)


tiles = np.array([1 if t=='^' else 0 for t in sys.stdin.readlines()[0].strip()])

kernel = np.array([1,0,1])

safe_tiles = tiles.size-tiles.sum(dtype=int)
for i in range(1,40):
    tiles = np.convolve(tiles, kernel, mode='same')%2
    safe_tiles += tiles.size-tiles.sum(dtype=int)
print('*1:',safe_tiles)

for i in range(40,400000):
    tiles = np.convolve(tiles, kernel, mode='same')%2
    safe_tiles += tiles.size-tiles.sum(dtype=int)
print('*2:',safe_tiles)
