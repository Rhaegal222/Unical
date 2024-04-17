N = input()
C = False
while N != '*':
    M = N
    N = input()
    if N == M:
        C = True
if C:
    print('SI', end='')
else:
    print('NO', end='')