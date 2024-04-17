def destra(matrice, lista, indice, righe, colonne, dim_mat, bord, riga, colonna):
    for i in range(colonna, colonne):
        if matrice[riga+bord][i] == '*':
            matrice[riga+bord][i] = lista[indice]
            indice += 1
            dim_mat += 1
            if indice >= len(lista):
                indice = 0
    colonna = i
    return dim_mat, indice, colonna, riga

def sotto(matrice, lista, indice, righe, colonne, dim_mat, bord, riga, colonna):
    for i in range(riga, righe):
        if matrice[i][colonna-bord] == '*':
            matrice[i][colonna-bord] = lista[indice]
            indice += 1
            dim_mat += 1
            if indice >= len(lista):
                indice = 0
    riga = i
    return dim_mat, indice, colonna, riga

def sinistra(matrice, lista, indice, righe, colonne, dim_mat, bord, riga, colonna):
    for i in range(colonne-1, -1, -1):
        if matrice[riga-bord][i] == '*':
            matrice[riga-bord][i] = lista[indice]
            indice += 1
            dim_mat += 1
            if indice >= len(lista):
                indice = 0
    colonna = i
    return dim_mat, indice, colonna, riga

def sopra(matrice, lista, indice, righe, colonne, dim_mat, bord, riga, colonna):
    for i in range(righe-1, -1, -1):
        if matrice[i][colonna+bord] == '*':
            matrice[i][colonna+bord] = lista[indice]
            indice += 1
            dim_mat += 1
            if indice >= len(lista):
                indice = 0
    riga = i
    return dim_mat, indice, colonna, riga
    
def main():
    k = int(input())
    lista = [int(input()) for i in range(k)]
    righe = int(input())
    colonne = int(input())
    matrice = [['*' for j in range(colonne)] for i in range(righe)]
    riga = 0
    colonna = 0
    indice = 0
    dim_mat = 0
    bord = 0

    while dim_mat < righe*colonne:
        dim_mat, indice, colonna, riga = destra(matrice, lista, indice, righe, colonne, dim_mat, bord, riga, colonna)
        dim_mat, indice, colonna, riga = sotto(matrice, lista, indice, righe, colonne, dim_mat, bord, riga, colonna)
        dim_mat, indice, colonna, riga = sinistra(matrice, lista, indice, righe, colonne, dim_mat, bord, riga, colonna)
        dim_mat, indice, colonna, riga = sopra(matrice, lista, indice, righe, colonne, dim_mat, bord, riga, colonna)
        bord += 1

    for i in range(righe):
        for j in range(colonne):
            print(matrice[i][j], end='')
        print()

main()