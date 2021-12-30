import sys


directions = [l.strip() for l in sys.stdin.readlines()]

moves = {
    'R': +1+0j,
    'U':  0+1j,
    'L': -1+0j,
    'D':  0-1j,
}


keypad = {
    -1+1j:'1', 0+1j:'2', 1+1j:'3',
    -1+0j:'4', 0+0j:'5', 1+0j:'6',
    -1-1j:'7', 0-1j:'8', 1-1j:'9',
}
position = 0+0j
code = ''
for d in directions:
    for m in d:
        if position+moves[m] in keypad:
            position += moves[m]
    code += keypad[position]
print('*1:',code)


keypad = {
                        2+2j:'1',
              1+1j:'2', 2+1j:'3', 3+1j:'4',
    0+0j:'5', 1+0j:'6', 2+0j:'7', 3+0j:'8', 4+0j:'9',
              1-1j:'A', 2-1j:'B', 3-1j:'C',
                        2-2j:'D',
}
position = 0+0j
code = ''
for d in directions:
    for m in d:
        if position+moves[m] in keypad:
            position += moves[m]
    code += keypad[position]
print('*2:',code)
