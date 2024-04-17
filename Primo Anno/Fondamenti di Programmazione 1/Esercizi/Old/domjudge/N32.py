X = int(input())
L = []
C = False
C1 = False
cont = 0
while X != 0:
    L.append(X)
    X = int(input())
if not C:
    for i in range(len(L) - 1):
        if L[i] < L[i + 1]:
            cont += 1
        else:
            C = True
            break
if C and cont > 0:
    for i in range(cont, len(L) - 1):
        if L[i] > L[i + 1]:
            C1 = True
        else:
            C1 = False
            break

if C and C1:
    print("SI", end="")
else:
    print("NO", end="")