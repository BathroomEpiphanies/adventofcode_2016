import sys
import re
import numpy as np


sides = np.array([[int(n) for n in re.findall(r'(\d+)',l)] for l in sys.stdin.readlines()])

print('*1:', sum(sum(s)>2*max(s) for s in sides))

sides = sides.T.reshape(-1,3)
print('*2:', sum(sum(s)>2*max(s) for s in sides))
