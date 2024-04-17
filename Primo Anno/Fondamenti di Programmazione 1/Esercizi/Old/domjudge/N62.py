A = []
Mat = []
K = int(input())

for i in range(K):
    A.append(int(input()))

N = int(input())
M = int(input())
for i in range(N):
    Mat.append([])
    for j in range(M):
        Mat[i].append(0)

iA = 0
cont = 0
cont2 = 1
while iA <= (N*M):
    #Compone la prima riga:
    for j in range(cont, M - cont):
        Mat[cont][j] = A[iA%len(A)]
        iA+=1

    if iA >= (N*M):
        break

    #Compone l'ultima colonna:
    for i in range(cont2, N - cont):
        Mat[i][M - cont2] = A[iA%len(A)]
        iA+=1

    if iA >= (N*M):
        break

    #compone l'ultima riga:
    for j in range(M-2-cont, -1 + cont, -1):
        Mat[N - cont - 1][j] = A[iA%len(A)]
        iA+=1

    if iA >= (N*M):
        break

    #compone la prima colonna:
    for i in range(N-2-cont, -1 + cont2, -1):
        Mat[i][cont] = A[iA%len(A)]
        iA+=1
    
    if iA >= (N*M):
       break

    cont += 1
    cont2 += 1
    
for i in range(N):
    for j in range(M):
        print(Mat[i][j], end='')
    print()
