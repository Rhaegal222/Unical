X = input()
L = list(X)
Len = int(len(L))
Len2 = int(len(L)/2)
Somma1= 0
Somma2= 0
for i in range(Len2):
    Somma1 = Somma1 + (int(L[i]))
for i in range(Len2, Len):
    Somma2 = Somma2 + (int(L[i]))
if Somma1 == Somma2:
    print('FORTUNATO', end="")
else:
    print('SFORTUNATO', end="")
