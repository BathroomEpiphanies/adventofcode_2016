import sys
import re


lines = [l.strip() for l in sys.stdin.readlines()]


def decompress_string(string):
    decompressed,remaining = '',string
    while remaining:
        m = re.search(r'\((\d+)x(\d+)\)',remaining)
        if not m:
            break
        decompressed += remaining[:m.span()[0]]
        decompressed += int(m.group(2))*remaining[m.span()[1]:m.span()[1]+int(m.group(1))]
        remaining = remaining[m.span()[1]+int(m.group(1)):]
    return decompressed+remaining
    
for line in lines:
    decompressed = decompress_string(line)
    #print(line)
    #print(len(decompressed))

print('*1:',len(decompressed))


def decompressed_length(string):
    m = re.search(r'\((\d+)x(\d+)\)',string)
    if not m:
        return len(string)
    pre = string[:m.span()[0]]
    mid = string[m.span()[1]:m.span()[1]+int(m.group(1))]
    pst = string[m.span()[1]+int(m.group(1)):]
    return \
        len(pre) + \
        int(m.group(2))*decompressed_length(mid) + \
        decompressed_length(pst)

for line in lines:
    length = decompressed_length(line)
    #print(line)
    #print(length)

print('*2:',length)
