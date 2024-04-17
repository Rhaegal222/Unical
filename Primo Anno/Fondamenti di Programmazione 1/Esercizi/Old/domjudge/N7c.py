N = int
N1 = 0
N2 = 0
N3 = 0
i = 0
s = ''

while N != 0:
    N = int(input())
    if N >= 1 and N <= 3 :
        s = s + str(N)
        i = i + 1
    if N == 1:
        N1 = N1 + 1
    elif N == 2:
        N2 = N2 + 1
    elif N == 3:
        N3 = N3 + 1

if s != '':
    X1 = round((N1 / i) * 100, 1)
    X2 = round((N2 / i) * 100, 1)
    X3 = round((N3 / i) * 100, 1)
    print(1, N1, X1)
    print(2, N2, X2)
    print(3, N3, X3)
    if ((X1 == X2) and (X3 < 50)) or ((X2 == X3) and (X1 < 50)) or ((X1 == X3) and (X2 < 50) ):
        print('BALLOTTAGGIO', end="")
    elif X1 > 50.0:
        print('VINCE 1', end="")
    elif X2 > 50.0:
        print('VINCE 2', end="")
    elif X3 > 50.0:
        print('VINCE 3', end="")
    else:
        print('BALLOTTAGGIO', end="")
elif s == '':
    print('BALLOTTAGGIO', end="")
