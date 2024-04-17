def dx(righe, colonne, lastpos, A, B, cont, cont2):
    for i in range(colonne, len(B[0])):
        if B[righe+cont2][i] == '*':
            B[righe+cont2][i] = A[lastpos]
            cont += 1
            lastpos += 1
            if lastpos==len(A):
                lastpos=0
    righe = i
    return cont, righe, lastpos
    
def sx(righe, colonne, lastpos, A, B, cont, cont2):
    for i in range(colonne, -1, -1):
        if B[righe-cont2][i] == '*':
            B[righe-cont2][i] = A[lastpos]
            cont += 1
            lastpos += 1
            if lastpos==len(A):
                lastpos=0
    righe = i
    return cont, righe, lastpos

def up(righe, colonne, lastpos, A, B, cont, cont2):
    for i in range(righe, -1, -1):
        if B[i][colonne+cont2] == '*':
            B[i][colonne+cont2] = A[lastpos]
            cont += 1
            lastpos += 1
            if lastpos==len(A):
                lastpos=0
    colonne = i
    return cont, colonne, lastpos

def down(righe, colonne, lastpos, A, B, cont, cont2):
    for i in range(righe, len(B)):
        if B[i][colonne-cont2] == '*':
            B[i][colonne-cont2] = A[lastpos]
            cont += 1
            lastpos += 1
            if lastpos==len(A):
                lastpos=0
    colonne = i
    return cont, colonne, lastpos

def main():
    K=int(input())
    A=[int(input()) for i in range(K)]
    
    N=int(input())  ## N righe
    M=int(input())  ## M colonne

    B=[['*' for j in range(M)] for i in range(N)] ##matrice

    righe=0 ##colonna iniziale
    colonne=0 ##riga iniziale
    lastpos=0 ##ultima posizione in cui abbiamo lasciato la lista

    cont = 0
    cont2 = 0

    while cont < N*M:
        cont, colonne, lastpos = dx(righe, colonne, lastpos, A, B, cont, cont2)
        cont, righe, lastpos = down(righe, colonne, lastpos, A, B, cont, cont2)
        cont, colonne, lastpos = sx(righe, colonne, lastpos, A, B, cont, cont2)
        cont, righe, lastpos = up(righe, colonne, lastpos, A, B, cont, cont2)
        cont2 += 1
    
    for i in range(N):
        for j in range(M):
            print(B[i][j], end="")
        print()

main()