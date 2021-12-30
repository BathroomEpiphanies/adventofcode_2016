import sys
import re


lines = [l.strip() for l in sys.stdin.readlines()]


def matches_abba(s):
    m = re.match(r'.*(\w)(\w)\2\1.*',s)
    return m and m.group(1)!=m.group(2)


count = 0
for line in lines:
    outside = re.sub(r'\[\w+\]','#',line)
    inside = '#'.join(s[1:-1] for s in re.findall(r'\[\w+\]',line))
    if matches_abba(outside) and not matches_abba(inside):
        count += 1

print('1*:',count)


count = 0
for line in lines:
    outside = re.sub(r'\[\w+\]','#',line)
    inside = '#'.join(s[1:-1] for s in re.findall(r'\[\w+\]',line))
    m = re.findall(r'(?=(\w)(\w)\1)',outside)
    for m in re.findall(r'(?=(\w)(\w)\1)',outside):
        if m[0]==m[1]:
            continue
        if re.match(fr'.*{m[1]}{m[0]}{m[1]}',inside):
            count += 1
            break

print('2*:',count)
