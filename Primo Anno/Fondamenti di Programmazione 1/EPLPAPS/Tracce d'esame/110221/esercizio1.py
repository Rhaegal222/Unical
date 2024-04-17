def main():
    direzione = input()
    righe = int(input())
    colonne = int(input())
    matrice = crea(righe, colonne, [], input())
    risultato = simulazione(direzione, matrice, righe, colonne)
    stampa(risultato)

def crea(righe, colonne, matrice, dati):
    dati = list(dati)
    for i in dati:
        if i == ' ':
            dati.remove(i)
    cont = 0
    for i in range(righe):
        matrice.append([])
        for j in range(colonne):
            matrice[i].append(int(dati[cont]))
            cont += 1
    return matrice

def simulazione(direzione, matrice, righe, colonne):
    if direzione == 'sud':
        matrice = sud(matrice, righe, colonne)
    elif direzione == 'nord':
        matrice = nord(matrice, righe, colonne)
    elif direzione == 'est':
        matrice = est(matrice, righe, colonne)
    elif direzione == 'ovest':
        matrice = ovest(matrice, righe, colonne)
    elif direzione == 'sud-est':
       matrice = sud(matrice, righe, colonne)
       matrice = est(matrice, righe, colonne)
    elif direzione == 'sud-ovest':
       matrice = sud(matrice, righe, colonne)
       matrice = ovest(matrice, righe, colonne)
    elif direzione == 'nord-est':
       matrice = nord(matrice, righe, colonne)
       matrice = est(matrice, righe, colonne)
    elif direzione == 'nord-ovest':
       matrice = nord(matrice, righe, colonne)
       matrice = ovest(matrice, righe, colonne)
    return matrice

def sud(matrice, righe, colonne):
    for i in range(righe):
        for j in range(colonne):
            if matrice[i][j] == 0 or matrice[i][j] == 3:
                if j>0 and matrice[i+1][j-1] == 1:
                    matrice[i+1][j-1] = 3
                if matrice[i+1][j] == 1:
                    matrice[i+1][j] = 3
                if j<colonne-1 and matrice[i+1][j+1] == 1:
                    matrice[i+1][j+1] = 3
    return matrice
        
def nord(matrice, righe, colonne):
    for i in range(righe-1, 0, 1):
        for j in range(colonne):
            if matrice[i][j] == 0 or matrice[i][j] == 3:
                if j>0 and matrice[i-1][j-1] == 1:
                    matrice[i-1][j-1] = 3
                if matrice[i-1][j] == 1:
                    matrice[i-1][j] = 3
                if j<colonne-1 and matrice[i-1][j+1] == 1:
                    matrice[i-1][j+1] = 3
    return matrice

def est(matrice, righe, colonne):
    for j in range(colonne-1):
        for i in range(righe):
            if matrice[i][j] == 0 or matrice[i][j] == 3:
                if i>0 and matrice[i-1][j+1] == 1:
                    matrice[i-1][j+1] = 3
                if matrice[i][j+1] == 1:
                    matrice[i][j+1] = 3
                if i<righe-1 and matrice[i+1][j+1] == 1:
                    matrice[i+1][j+1] = 3
    return matrice

def ovest(matrice, righe, colonne):
    for j in range(colonne-1,0,-1):
        for i in range(righe):
            if matrice[i][j] == 0 or matrice[i][j] == 3:
                if i>0 and matrice[i-1][j-1] == 1:
                    matrice[i-1][j-1] = 3
                if matrice[i][j-1] == 1:
                    matrice[i][j-1] = 3
                if i<righe-1 and matrice[i+1][j-1] == 1:
                    matrice[i+1][j-1] = 3
    return matrice

def stampa(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == 0:
                print('O ', end='')
            elif matrice[i][j] == 1:
                print('_ ', end='')
            elif matrice[i][j] == 2:
                print('# ', end='')
            elif matrice[i][j] == 3:
                print('* ', end='')
        print()

main()