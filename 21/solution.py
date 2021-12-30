import sys
import re
import itertools


lines = [l.strip() for l in sys.stdin.readlines()]


password = lines[0]
hashed = lines[1]
instructions = lines[2:]

def scramble(instructions,password):
    for instruction in instructions:
        #print(password)
        #print(instruction)
        m = re.match(r'swap position (\d+) with position (\d+)', instruction)
        if m:
            x,y = sorted(int(n) for n in m.groups())
            password = password[:x]+password[y]+password[x+1:y]+password[x]+password[y+1:]
            continue
        
        m = re.match(r'swap letter (\w) with letter (\w)', instruction)
        if m:
            password = password.translate(str.maketrans(''.join(m.groups()),''.join(m.groups()[::-1])))
            continue
    
        m = re.match(r'rotate (left|right) (\d+) steps?', instruction)
        if m:
            n = {'left':1,'right':-1}[m.group(1)]*int(m.group(2))%len(password)
            password = password[n:]+password[:n]
            continue
    
        m = re.match(r'rotate based on position of letter (\w)', instruction)
        if m:
            n = password.index(m.group(1))
            n = (n+(2 if n>3 else 1))%len(password)
            password = password[-n:]+password[:-n]
            continue
    
        m = re.match(r'reverse positions (\d+) through (\d+)', instruction)
        if m:
            x,y = (int(n) for n in m.groups())
            password = password[:x]+''.join(reversed(password[x:y+1]))+password[y+1:]
            continue
    
        m = re.match(r'move position (\d+) to position (\d+)', instruction)
        if m:
            x,y = (int(n) for n in m.groups())
            if x<y:
                password = password[:x]+password[x+1:y+1]+password[x]+password[y+1:]
            else:
                password = password[:y]+password[x]+password[y:x]+password[x+1:]
            continue
    return password


print('*1:',scramble(instructions,password))


for password in (''.join(p) for p in itertools.permutations(hashed)):
    if hashed == scramble(instructions,password):
        print('*2:',password)
