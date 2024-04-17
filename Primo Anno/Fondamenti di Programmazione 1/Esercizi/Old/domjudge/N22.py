N = 0
S = False
while N != '.':
    N = input()
    if N.isalpha() :
        S = True
if S:
    print('SI', end="")
else:
    print('NO', end="")