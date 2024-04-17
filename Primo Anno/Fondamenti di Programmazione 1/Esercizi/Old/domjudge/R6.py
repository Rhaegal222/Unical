def main():
    N = int(input())
    matrice = crea_matrice(N)
    lista = lista_sommaL([], N, matrice, 0, 0, 0)
    diagonale_secondaria = []
    trova_diagonale_secondaria(diagonale_secondaria, matrice, 0, 0, 0)
    verifica_multiplo(lista, diagonale_secondaria)

def crea_matrice(N):
    matrice = []
    for i in range(N):
        matrice.append([])
        for j in range(N):
            matrice[i].append(int(input()))
    return matrice

def lista_sommaL(lista, N, matrice, x, y, cont):
    if y == N-1:
        return lista
    if y < N:
        lista.append(somma_L(matrice, x, y, cont))
    return lista_sommaL(lista, N, matrice, x, y+1, cont + 1)

def somma_L(matrice, i, j, cont):
    if i < len(matrice)-1-cont:
        return matrice[i][j] + somma_L(matrice, i+1, j, cont)
    if j < len(matrice)-1:
        return matrice[i][j] + somma_L(matrice, i, j+1, cont)
    return matrice[i][j]

def trova_diagonale_secondaria(diagonale_secondaria, matrice, i, j, cont):
    if cont >= len(matrice)-1:
        return diagonale_secondaria
    if i == len(matrice)-1-cont:
        diagonale_secondaria.append(matrice[i][j])
        return trova_diagonale_secondaria(diagonale_secondaria, matrice, 0, j+1, cont+1)
    return trova_diagonale_secondaria(diagonale_secondaria, matrice, i+1, j, cont)

def verifica_multiplo(lista, diagonale_secondaria):
    condizione = True
    for i in range(len(lista)):
        if lista[i] % diagonale_secondaria[i] == 0:
            condizione = True
        else:
            condizione = False
            break
    if condizione:
        print('SI', end='')
    else:
        print('NO', end='')
main()