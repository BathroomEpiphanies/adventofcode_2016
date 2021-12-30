import sys
import re
from hashlib import md5
import itertools
import collections


salt = sys.stdin.readlines()[0].strip()


def simple_hash(h):
    return md5(h.encode()).hexdigest()

hash_generator = ( (i,simple_hash(f'{salt}{i}')) for i in itertools.count() )
queue = collections.deque(maxlen=1000)
for i,h in zip(range(1000),hash_generator):
    queue.append(h)

keys = []
while len(keys)<64:
    i,cand = queue.popleft()
    queue.append(next(hash_generator))
    m = re.match(r'.*?(\w)\1\1.*',cand)
    if m and any(re.match(rf'.*{m.group(1)}{{5}}.*',h) for _,h in queue):
        keys.append(cand)

print('*1:',i)


def stretch_hash(h):
    for i in range(2017):
        h = md5(h.encode()).hexdigest()
    return h

hash_generator = ( (i,stretch_hash(f'{salt}{i}')) for i in itertools.count() )
queue = collections.deque(maxlen=1000)
for i,h in zip(range(1000),hash_generator):
    queue.append(h)

keys = []
while len(keys)<64:
    i,cand = queue.popleft()
    queue.append(next(hash_generator))
    m = re.match(r'.*?(\w)\1\1.*',cand)
    if m and any(re.match(rf'.*{m.group(1)}{{5}}.*',h) for _,h in queue):
        keys.append(cand)

print('*2:',i)
