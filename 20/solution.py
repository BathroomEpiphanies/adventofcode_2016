import sys


ranges = [(int(a),int(b)) for a,b in (l.strip().split('-') for l in sys.stdin.readlines())]


ranges.sort()

u = 0
for a,b in ranges:
    if u<a:
        print('*1:',u)
        break
    else:
        u = max(u,b+1)

u = 0
allowed_count = 0
for a,b in ranges:
    if u<a:
        allowed_count += a-u
    u = max(u,b+1)
allowed_count += (4294967295+1)-u
print('*2:',allowed_count)
