N = None
L = []

while True:
    N = int(input())
    if N < 0:
        break
    else:
        L.append(N)

if len(L) > 0:
    L1 = ''
    M = L[0]
    for i in L:
        if i >= M:
            L1 += str(i)
        else:
            L1 += str('.')
            L1 += str(i)
        M = i

    Stringa = L1.split('.')
    cont = 0
    Stringa1 = ''
    for i in Stringa:
        if len(i) > cont:
            cont = len(i)
            Stringa1=''
            Stringa1 += i
            
    print(Stringa1, sep='')
    print(cont, end='')
            
else:
    print('Empty', end='')
