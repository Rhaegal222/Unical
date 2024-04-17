def main():
    n = int(input())
    matrice = [[int(input()) for j in range(n)] for i in range (n)]
    print('SI' if scan(matrice, 0, 0, 0, n-1, 0) else 'NO', end='')

def scan(matrice, i, j, sum, righe, colonne):
    if i < righe:
        sum += matrice[i][j+colonne]
        return scan(matrice, i+1, j, sum, righe, colonne)
    elif j <= righe:
        sum += matrice[i][j+colonne]
        return scan(matrice, i, j+1, sum, righe, colonne)
    else:
        if sum % matrice[righe][colonne] != 0:
            return False
        if righe > 0:
            return scan(matrice, 0, 0, 0, righe-1, colonne+1)
        return True
        
main()