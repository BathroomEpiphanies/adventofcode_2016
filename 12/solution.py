import sys


def run_program(a,b,c,d):
    a = 1
    b = 1
    d = 26
    
    if c != 0:
        c = 7
        while c != 0:
            d += 1
            c -= 1
    
    while d != 0:
        c = a
        while b != 0:
            a += 1
            b -= 1
        b = c
        d -= 1
    
    c = 16
    while c != 0:
        d = 17
        while d != 0:
            a += 1
            d -= 1
        c -= 1
    
    return a,b,c,d


print('*1:', run_program(0,0,0,0)[0])
print('*2:', run_program(0,0,1,0)[0])
