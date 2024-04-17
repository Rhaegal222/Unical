def main():
    k = int(input())
    numeri = [int(input()) for i in range(k)]
    righe = int(input())
    colonne = int(input())
    create(numeri, righe, colonne, 0, 0)

def create(numeri, righe, colonne, riga, colonna):
    area = 0
    cont = 0
    cont1 = 0
    matrice = []
    for i in range(righe):
        matrice.append([])
        for j in range(colonne):
            matrice[i].append(' ')

    while area < righe*colonne:
        
        for j in range(colonna, colonne-cont1):
            if area < righe*colonne and matrice[riga+cont1][j] == ' ':
                matrice[riga+cont1][j] = (numeri[cont]) 
                cont += 1
                area += 1
            if cont >= len(numeri):
                cont = 0
        colonna = j

        for i in range(riga+1+cont1, righe):
            if area < righe*colonne and matrice[i][colonna] == ' ':
                matrice[i][colonna]= (numeri[cont])
                cont += 1
                area += 1
            if cont >= len(numeri):
                cont = 0
        riga = i

        for j in range(colonna-1, -1, -1):
            if area < righe*colonne and matrice[riga-cont1][j] == ' ':
                matrice[riga-cont1][j] = (numeri[cont])
                cont += 1
                area += 1
            if cont >= len(numeri):
                cont = 0
        colonna = j

        for i in range(riga-1-cont1, -1, -1):
            if area < righe*colonne and matrice[i][colonna] == ' ':
                matrice[i][colonna] = (numeri[cont])
                cont += 1
                area += 1
            if cont >= len(numeri):
                cont = 0
        riga = i

        cont1 += 1

    for i in range(righe):
        for j in range(colonne):
            print(matrice[i][j], end='')
        print()
main()