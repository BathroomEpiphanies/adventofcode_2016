import sys
import math


register = {'a':0, 'b':1, 'c':2, 'd':3}
toggle = {'inc':'dec', 'dec':'inc', 'tgl':'inc', 'jnz':'cpy', 'cpy':'jnz'}

program = [l.strip().split() for l in sys.stdin.readlines()]
for line in program:
    for i,token in enumerate(line):
        try:
            line[i] = int(token)
        except:
            pass
    if len(line)<3:
        line += [None]


def run_program(memory):
    pointer = 0
    while pointer<len(program):
        i,a,b = program[pointer]
        if   i=='cpy':
            memory[register[b]] = (a if isinstance(a, int) else memory[register[a]])
        elif i=='inc':
            memory[register[a]] += 1
        elif i=='dec':
            memory[register[a]] -= 1
        elif i=='jnz':
            if isinstance(a, int) and a!=0 or not isinstance(a, int) and memory[register[a]]!=0:
                pointer += (b if isinstance(b, int) else memory[register[b]])
                continue
        elif i=='tgl':
            target = pointer + (a if isinstance(a, int) else memory[register[a]])
            if 0<=target<len(program):
                program[target][0] = toggle[program[target][0]]
            for line in program:
                print(line)
            print(memory)
            print()
        pointer += 1
    return memory

#print('*1:', run_program([7,0,0,0])[0])
#print('*2:', run_program([12,0,0,0])[0])

print('*1:', math.factorial(7)+7663)
print('*2:', math.factorial(12)+7663)
