def main():
    n = int(input())
    matrice = inserimento(n, [])
    matrice_inv = inv(matrice, n, [])
    righe = scan(matrice, n)
    colonne = scan(matrice_inv, n)
    print('SI' if righe and colonne else 'NO', end='')

def inserimento(n, matrice):
    for i in range(n):
        matrice.append([])
        for j in range(n):
            matrice[i].append(int(input()))
    return matrice

def scan(matrice, n):
    for i in range(n):
        for j in range(n):
            if matrice[i].count(matrice[i][j])>1:
                return False
    return True

def inv(matrice, n, matrice_inv):
    for i in range(n-1, -1, -1):
        matrice_inv.append([])
        for j in range(n):
            matrice_inv[n-i-1].append(matrice[j][i])
    return matrice_inv


main()