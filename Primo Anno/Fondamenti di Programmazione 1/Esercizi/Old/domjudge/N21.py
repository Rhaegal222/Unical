N = 0
S = False
while N != '.':
    N = input()
    if N.isalpha():
        S = True
if S:
    print('NO', end="")
else:
    print('SI', end="")