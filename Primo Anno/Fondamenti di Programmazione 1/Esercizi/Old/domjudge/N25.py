L = []
N = None
cont=0
Somma = 0
while True:
    N = int(input())
    L.append(N)
    if N == 0:
        cont += 1
    else:
        cont = 0
    if cont >= 2:
        break
for i in range(len(L)-1):
    if L[i] != 0:
        Somma = Somma + L[i]
    else:
        print(Somma)
        Somma = 0
