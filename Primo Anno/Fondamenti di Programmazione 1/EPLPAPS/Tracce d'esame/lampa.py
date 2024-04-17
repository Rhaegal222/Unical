from random import randint

def stampa(matrice):
    for i in range(len(matrice)): 
        for j in range(len(matrice[i])):
            print(matrice[i][j], end='')
        print()

def scan(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                return False
    return True

def modifica(matrice, x, y):
    #centrale
    if matrice[x][y] == 0:
        matrice[x][y] = 1
    else:
        matrice[x][y] = 0
    
    #sopra
    if x > 0 and matrice[x-1][y] == 0:
        matrice[x-1][y] = 1
    elif x > 0 and matrice[x-1][y] == 1:
        matrice[x-1][y] = 0
    
    #sotto
    if x < len(matrice)-1 and matrice[x+1][y] == 0:
        matrice[x+1][y] = 1
    elif  x < len(matrice)-1 and matrice[x+1][y] == 1:
        matrice[x+1][y] = 0
    
    #destra
    if y < len(matrice)-1 and matrice[x][y+1] == 0:
        matrice[x][y+1] = 1
    elif y < len(matrice)-1 and matrice[x][y+1] == 1:
        matrice[x][y+1] = 0
    
    #sinistra
    if y > 0 and matrice[x][y-1] == 0:
        matrice[x][y-1] = 1
    elif y > 0 and matrice[x][y-1] == 1:
        matrice[x][y-1] = 0
    
    return matrice

def gioca(matrice, vittoria):
    stampa(matrice)
    x = int(input('Inserisci la riga: '))
    y = int(input('Inserisci la colonna: '))
    
    matrice = modifica(matrice, x, y)
    vittoria = scan(matrice)
    
    if vittoria:
        print('Hai Vinto!')
    else:
        return gioca(matrice, vittoria)

def main():
    n = int(input('Inserisci la dimensione della matrice: '))
    #matrice = [[0, 0, 1, 0],[0, 1, 1, 1],[0, 0, 1, 0],[0, 0, 0, 0]]
    matrice = [[randint(0, 1) for j in range(n)] for i in range(n)]
    gioca(matrice, False)

main()