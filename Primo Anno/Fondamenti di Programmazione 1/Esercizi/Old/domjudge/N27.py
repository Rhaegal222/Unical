X = int(input())
N = 0
cont = 0
while N != -1:
    N = int(input())
    if N != -1:
        if N <= X:
            cont += 1
        if N > X and cont < X:
            cont = 0
if cont >= X:
    print('OK', end="")
else:
    print('NO', end="")
