X = int(input())
cont = 1
L = []
test1 = True
test2 = False
Lm = -1
while cont <= X:
    N = int(input())
    L.append(N)
    cont += 1
Y = int(len(L))
for i in range(0, Y, 2):
    if test1:
        if L[i] > Lm:
            test1 = True
        else:
            test1 = False
    Lm = L[i]
for i in range(1, Y, 2):
    if L[i] % 2 != 0:
        test2 = True
if (test1 == True and test2 == True) or Lm == -1:
    print("SI", end="")
else:
    print("NO", end="")
