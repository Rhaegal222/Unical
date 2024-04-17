cont = 0
L = []
Condizione = True
for i in range(10):
    N = int(input())
    cont += 1
    L.append(N)
X = int(input())
if Condizione:
    for i in range(len(L)):
        if L[i] % X == 0:
            Condizione = False
if Condizione:
    print('OK', end='')
else:
    print('NO', end='')
