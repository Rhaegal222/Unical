def stampa(tabella):
    for i in range(len(tabella)):
        print('|', end='')
        for j in range(len(tabella[0])):
            if tabella[i][j] == 1:
                print('X'+'|', end='')
            elif tabella[i][j] == 2:
                print('O'+'|', end='')
            else:
                print(' '+'|', end='') 
        print()

def controllo(tabella, colonna):
    x, y = 0, colonna
    for i in range(len(tabella)):
        if tabella[i][colonna] != 0:
            x = i
            break
#--------------------Ragno---------------------#
    cont = 0
    for i in range(y, y+4): #destra
        if i >= len(tabella[0]) or tabella[x][i] != tabella[x][y]:
            break
        else:
            newy = i
            cont+=1
    
    if cont < 4:
        cont = 0
        for i in range(newy, newy-4, -1): #sinistra
            if i < 0 or tabella[x][i] != tabella[x][newy]:
                break
            else:
                cont+=1
    
    if cont < 4:
        cont = 0
        for i in range(x, x+4): #diagonale-destra
            if i >= len(tabella) or (y+i) >= len(tabella[0]) or tabella[i][y+i] != tabella[x][y]:
                break
            else:
                cont+=1
    
    if cont < 4:
        cont = 0
        for i in range(x, x+4): #diagonale-sinistra
            if i >= len(tabella) or (x+y-i) < 0 or tabella[i][x+y-i] != tabella[x][y]:
                break
            else:
                cont+=1
    
    if cont < 4:
        cont = 0
        for i in range(x, x+4): #sotto
            if i >= len(tabella) or tabella[i][y] != tabella[x][y]:
                break
            else:
                cont+=1
    if cont < 4:
        return None
    return tabella[x][y]

def gioca(righe, colonne, tabella):
    vincitore, red_tok, blu_tok = None, 0, 0
    while vincitore == None and red_tok+blu_tok<righe*colonne:
        tabella, colonna = putinto(righe, colonne, tabella, 1)
        red_tok += 1
        stampa(tabella)
        if red_tok > 3:
            vincitore = controllo(tabella, colonna)
        if vincitore == None:
            tabella, colonna = putinto(righe, colonne, tabella, 2)
            blu_tok += 1
            stampa(tabella)
            if blu_tok > 3:
                vincitore = controllo(tabella, colonna)
        else:
            return vincitore
    return vincitore

def putinto(righe, colonne, tabella, giocatore):
    print('BLU' if giocatore == 1 else 'ROSSO', 'Inserisci la colonna:', 0, '-', colonne-1,': ', end='')
    colonna = int(input())
    if colonna < 0 or colonna > colonne-1:
        print('BLU' if giocatore == 1 else 'ROSSO', 'Inserisci la colonna:', 0, '-', colonne-1,': ', end='')
        colonna = int(input())

    F_insert = True
    
    for i in range(righe-1, -1, -1):
        if tabella[i][colonna] == 0:
            tabella[i][colonna] = giocatore
            F_insert = False
            break
    
    if F_insert:
        return putinto(righe, colonne, tabella, giocatore)
    else:
        return tabella, colonna

def crea():
    righe = int(input('Quante righe? (min righe: 4): '))
    while righe<4:
        righe = int(input('Inserisci un numero >= 4: '))
    colonne = int(input('Quante colonne? (min colonne: 4): '))
    while colonne<4:
        colonne = int(input('Inserisci un numero >= 4: '))
    tabella = [[0 for j in range(colonne)] for i in range(righe)]
    return righe, colonne, tabella

def main():
    righe, colonne, tabella = crea()
    vincitore = gioca(righe, colonne, tabella)
    if vincitore == 1:
        print('VINCE BLU')
    elif vincitore == 2:
        print('VINCE ROSSO')
    else:
        print('PATTA')

main()