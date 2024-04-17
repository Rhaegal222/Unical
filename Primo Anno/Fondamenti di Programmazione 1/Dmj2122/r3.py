def main():
    n = int(input())
    matrice = [[int(input()) for j in range(n)] for i in range(n)]
    print(non_ricorsiva(matrice),';',ricorsiva(matrice, len(matrice)-1, 0, 0), sep='', end='')

def ricorsiva(matrice, i, j, somma):
    if i >= 0:
        if i+j == len(matrice)-1:
            somma += matrice[i][j]
        return ricorsiva(matrice, i-1, j+1, somma)
    else:
        return somma

def non_ricorsiva(matrice):
    somma = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i + j == len(matrice)-1:
                somma += matrice[i][j]
    return somma

main()