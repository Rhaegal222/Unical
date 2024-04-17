N = int(input())
Multiplo = False
Pari = False
while N != 0:
    M = N
    N = int(input())
    if N == 0:
        break
    Somma = N + M
    if N % 2 == 0 and M % 2 == 0:
        Pari = True
    elif Somma % N == 0 or Somma % M == 0:
        Multiplo = True
if Multiplo or Pari:
    print('SI', end="")
else:
    print('NO', end="")
