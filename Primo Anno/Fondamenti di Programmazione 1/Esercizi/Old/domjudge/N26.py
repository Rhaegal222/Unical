N = input()
C = False
while N != '*':
    M = N
    N = input()
    if (M.isupper() and N.isupper()) or (M == N and N.islower() and N.islower()):
        C = True
if C:
    print('SI', end='')
else:
    print('NO', end='')