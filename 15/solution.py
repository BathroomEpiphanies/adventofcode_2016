import sys
import re
import functools
import operator


discs = []
for line in sys.stdin.readlines():
    discs.append( [int(n) for n in re.match(r'Disc #(?:\d+) has (\d+) positions; at time=0, it is at position (\d+).', line).groups()] )


def chinese_remainder(equations):
    # Input: equations = [(remainder 1,divisor 1), (r2,d2) , ...]
    # Output: x satisfying | x = r mod d | for all equations
    N = functools.reduce(operator.mul, (d for r,d in equations))
    return sum(pow(N//d,-1,d)*(N//d)*r for r,d in equations)%N


equations = [ (-(1+i)-r, d) for i,(d,r) in enumerate(discs) ]
print('*1:',chinese_remainder(equations))

equations.append( (-(1+len(equations))-0, 11) )
print('*2:',chinese_remainder(equations))
