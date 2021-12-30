import sys
from collections import Counter

rows = [l.strip() for l in sys.stdin.readlines()]
counts = [Counter(c) for c in zip(*rows)]

print(''.join([max((d for d in c.items()), key=lambda x:x[1])[0] for c in counts]))
print(''.join([min((d for d in c.items()), key=lambda x:x[1])[0] for c in counts]))
