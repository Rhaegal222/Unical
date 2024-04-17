N = 0
S = ''
while N != '.':
    N = input()
    if N != '.':
        S = S + N
if S.isalpha() or S == '':
    print('SI', end="")
else:
    print('NO', end="")