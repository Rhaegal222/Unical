def main():
    n = int(input())
    matrice = composizione([], n)
    colonna = inserimento(n, [])
    riga = inserimento(n, [])
    newr, newc = scan(matrice, [], [])
    print('SI' if newr == riga and newc == colonna else 'NO', end='')

def stampa(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            print(matrice[i][j], end='')
        print()

def inserimento(n, lista):
    for i in range(n):
        lista.append(int(input()))
    return lista

def composizione(matrice, n):
    for i in range(n):
        matrice.append([])
        for j in range(n):
            matrice[i].append(int(input()))
    return matrice

def scan(matrice, newr, newc):
    contr = 0
    for i in range(len(matrice)):
        contr = 0
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                contr += 1
        newr.append(contr)
    
    contc = 0

    for i in range(len(matrice)):
        contc = 0
        for j in range(len(matrice)):
            if matrice[j][i] == 1:
                contc += 1
        newc.append(contc)
    
    return newr, newc


main()