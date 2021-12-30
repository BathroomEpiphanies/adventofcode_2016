import sys


lines = [l.strip() for l in sys.stdin.readlines()]


def dragon(memory,length):
    while len(memory)<length:
        memory = memory+'0'+memory.translate(str.maketrans('01','10'))[::-1]
    return memory[:length]

def checksum(memory):
    while len(memory)%2 == 0:
        memory = ''.join( ['1' if a==b else '0' for a,b in zip(memory[::2],memory[1::2])] )
    return memory


memory = lines[0]
disksize = int(lines[1])
print('*1:', checksum(dragon(memory,disksize)))


memory = lines[0]
disksize = 35651584
print('*2:', checksum(dragon(memory,disksize)))
