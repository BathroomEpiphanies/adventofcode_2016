import sys
import re
from collections import Counter


rooms = [re.match(r'(?P<name>[-\w]+)-(?P<sector>\d+)\[(?P<checksum>\w+)\]',l).groupdict() for l in sys.stdin.readlines()]


sum_real_sectors = 0
real_rooms = []
for room in rooms:
    counts = [(v,k) for k,v in Counter(room['name'].replace('-','')).items()]
    checksum = ''.join([c for _,c in sorted(counts,key=lambda x:(-x[0],x[1]))[:5]])
    if checksum == room['checksum']:
        sum_real_sectors += int(room['sector'])
        real_rooms.append(room)

print('*1:',sum_real_sectors)


secret_sector = None
for room in real_rooms:
    shift = int(room['sector'])
    name = ''.join(' ' if c=='-' else
                   chr((ord(c)-ord('a')+shift)%(1+ord('z')-ord('a'))+ord('a'))
                   for c in room['name'])
    if name == 'northpole object storage':
        secret_sector = room['sector']

print('*2:',secret_sector)

