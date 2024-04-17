def main():
    X = int(input())
    numeri = [i for i in range(1, X+1)]
    matrice = crea_matrice(X, numeri)
    print(diagonale_secondaria(matrice), end='')

def crea_matrice(X, numeri):
    matrice = []
    cont = 0
    for i in range(10):
        matrice.append([])
        for j in range(10):
            if cont == X:
                cont = 0
            matrice[i].append(numeri[cont])
            cont += 1
    return matrice

def stampa_matrice(matrice):
    for i in range(10):
        for j in range(10):
            print(matrice[i][j], '', end='')
        print()
    
def diagonale_secondaria(matrice):
    Somma = 0
    for i in range(10):
        for j in range(10):
            if i + j == 9:
                Somma += matrice[i][j]
    return Somma

main()