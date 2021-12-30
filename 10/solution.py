import sys
import re
from collections import defaultdict


lines = [l.strip() for l in sys.stdin.readlines()]


bots = defaultdict(lambda:{'hgh':None, 'low':None, 'chips':[], 'capacity':2})
for line in lines:
    m = re.match(r'(\w+ \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', line)
    if m:
        bots[m.group(1)]['low'] = m.group(2)
        bots[m.group(1)]['hgh'] = m.group(3)
    m = re.match(r'value (\d+) goes to (\w+ \d+)', line)
    if m:
        bots[m.group(2)]['chips'].append(int(m.group(1)))
bots.default_factory = lambda:{'hgh':None, 'low':None, 'chips':[], 'capacity':float('inf')}


compare_61_17 = None
while True:
    try:
        name = next(name for name,info in bots.items() if len(info['chips'])>=info['capacity'])
    except StopIteration:
        break
    bot = bots[name]
    if set(bot['chips']) == {17,61}:
        compare_61_17 = name
    bots[bot['low']]['chips'].append(min(bot['chips'][:2]))
    bots[bot['hgh']]['chips'].append(max(bot['chips'][:2]))
    bot['chips'] = bot['chips'][2:]


print('*1:', compare_61_17.split(' ')[1])
print('*2:', bots['output 0']['chips'][0]*bots['output 1']['chips'][0]*bots['output 2']['chips'][0] )
