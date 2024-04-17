N = 0
mat = []
SommaCroce = 0
SommaAltri = 0
while N < 3:
    N = int(input())

for i in range(N):
    mat.append([])
    for j in range(N):
        mat[i].append(int(input()))

for i in range(N):
    for j in range(N):
        if i == N // 2:
            SommaCroce = SommaCroce + mat[i][j]
        elif j == N // 2:
            SommaCroce = SommaCroce + mat[i][j]
        else:
            SommaAltri = SommaAltri + mat[i][j]

if SommaCroce > SommaAltri:
    print('OK', end='')
else:
    print('NO', end='')