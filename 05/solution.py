import sys
from hashlib import md5
from itertools import count,islice


doorid = sys.stdin.readlines()[0].strip()


hash_generator = ((h[5],h[6]) for h in (md5(f'{doorid}{i}'.encode()).hexdigest() for i in count()) if h[:5]=='00000')
password1 = ''
password2 = 8*[' ']
print(f'\r*1: {password1:8}    *2: {"".join(password2)}', end='')
while any(c==' ' for c in password2) or len(password1)<8:
    h5,h6 = next(hash_generator)
    if len(password1)<8:
        password1 += h5
    p = int(h5,16)
    if p<8 and password2[p]==' ':
        password2[p] = h6
    print(f'\r*1: {password1:8}    *2: {"".join(password2)}', end='')
print()
    
