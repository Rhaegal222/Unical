K = int(input())
A = [int(input()) for i in range(K)]
N = int(input()) #righe
M = int(input()) #colonne

mat = []

for i in range(N):
    mat.append([])
    for j in range(M):
        mat[i].append(0)

indA = 0
lenA = len(A)

verso = 1 #sinistra-destra sopra-sotto sinistra-destra sotto-sopra


modRigheSu = 0
modRigheGiu = 0
modColonneDestra = 0
modColonneSinistra = 0

col = 0
rig = 0

contOp = N * M

while contOp != 0:
    if verso == 1:
        for i in range(col, M - modColonneDestra, 1):
            if indA == lenA:
                indA = 0
            mat[rig][i] = A[indA]
            indA += 1
            contOp -= 1
        modRigheSu += 1
        col = M - modColonneDestra - 1
        rig += 1

    elif verso == 3:
        for i in range(col, modColonneSinistra - 1, -1):
            if indA == lenA:
                indA = 0
            mat[rig][i] = A[indA]
            indA += 1
            contOp -= 1
        modRigheGiu += 1
        col = modColonneSinistra
        rig -= 1

    elif verso == 2:
        for i in range(rig, N - modRigheGiu, 1):
            if indA == lenA:
                indA = 0
            mat[i][col] = A[indA]
            indA += 1
            contOp -= 1
        modColonneDestra += 1
        rig = N - modRigheGiu - 1
        col -= 1

    elif verso == 4:
        for i in range(rig, modRigheSu - 1, -1):
            if indA == lenA:
                indA = 0
            mat[i][col] = A[indA]
            indA += 1
            contOp -= 1
        modColonneSinistra += 1
        rig = modRigheSu
        col += 1

    verso += 1
    if verso == 5:
        verso = 1


for i in range(N):
    for j in range(M):
        print(mat[i][j], end = "") 
    print()