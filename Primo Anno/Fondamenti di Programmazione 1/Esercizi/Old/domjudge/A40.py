L = []
N = 0
L2 = []
while N != -50:
    N = int(input())
    if N < 1000 and N != -50:
        L.append(N)
if N == -50 and len(L) == 0:
    print('VUOTA', end="")
else:
    M = sum(L) // len(L)
    for i in L:
        if M <= i:
            L2.append(i)
    print(min(L2), end="")
