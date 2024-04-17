N = input()
C = False
while N != '*':
    M = N
    N = input()
    if N == M and (N.isalpha() and M.isalpha()) and ((N.islower() and N.islower()) or (N.isupper() and N.isupper())):
        C = True
if C:
    print('SI', end='')
else:
    print('NO', end='')