from random import randint
def stampa(griglia):
    for i in range(len(griglia)):
        for j in range(len(griglia)):
            if griglia[i][j] == 0:
                print('| ', end='')
            elif griglia[i][j] == 1:
                print('|X', end='')
            elif griglia[i][j] == 2:
                print('|O', end='')
        print('|')

def controllo_facile(griglia):
    for i in range(len(griglia)//2, -1, -1):
        for j in range(len(griglia)):
            print(griglia[i][j])

    #DIAGONALE PRINCIPALE
    cont = 1
    for i in range(len(griglia)):
        for j in range(len(griglia)-i):
            for k in range(i, len(griglia)):
                if j == k-i and j + 1 < len(griglia) and k + 1 < len(griglia) and griglia[j][k] == griglia[j+1][k+1]:
                    cont += 1
        if cont >= 4:
            return False
        else:
            cont = 1

    #DIAGONALE SECONDARIA
    cont = 1
    for i in range(len(griglia)):
        for j in range(len(griglia)-i):
            for k in range(len(griglia)-1-i, -1, -1):
                if j + k == len(griglia)-1-i and j+1 < len(griglia) and k - 1 >= 0 and griglia[j][k] == griglia[j+1][k-1]:
                    cont += 1
                    break
        if cont >= 4:
            return False
        else:
            cont = 1

    #colonna
    cont = 1
    for i in range(len(griglia)):
        for j in range(len(griglia)-1):
            if griglia[j][i] == griglia[j+1][i]:
                cont += 1
            elif cont >= 4:
                return False
            else: 
                cont = 1

    #riga
    cont = 1
    for i in range(len(griglia)):
        for j in range(len(griglia)-1):
            if griglia[i][j] == griglia[i][j+1]:
                cont += 1
            elif cont >= 4:
                return False
            else:
                cont = 1
    
    return True

def controllo(x, y, griglia):
    #diagonale principale
    cont = 1
    for i in range(len(griglia)):
        if (x+i < len(griglia)-1 and y+i < len(griglia)-1) and griglia[x+i+1][y+i+1] != 0 and griglia[x+i][y+i] == griglia[x+i+1][y+i+1]:
            cont += 1
        else:
            nuova_x = x+i
            nuova_y = y+i
            break
    if cont >= 4:
        return True

    #diagonale principale ritorno
    cont = 1
    for i in range(len(griglia)):
        if (nuova_x-i > 0 and nuova_y-i > 0) and griglia[nuova_x-i-1][nuova_y-i-1] != 0 and griglia[nuova_x-i][nuova_y-i] == griglia[nuova_x-i-1][nuova_y-i-1]:
            cont += 1
        else:
            break
    if cont >= 4:
        return True
    
    #diagonale secondaria
    cont = 1
    for i in range(len(griglia)):
        if (x+i < len(griglia) and y-i > 0) and griglia[x+i-1][y-i-1] != 0 and griglia[x+i][y+i] == griglia[x+i+1][y+i+1]:
            cont += 1
        else:
            nuova_x = x-i
            nuova_y = y-i
            break
    if cont >= 4:
        return True

    #diagonale secondaria ritorno
    cont = 1
    for i in range(len(griglia)):
        if (nuova_x-i > 0 and nuova_y-i > 0) and griglia[nuova_x-i-1][nuova_y-i-1] != 0 and griglia[nuova_x-i][nuova_y-i] == griglia[nuova_x-i-1][nuova_y-i-1]:
            cont += 1
        else:
            break
    if cont >= 4:
        return True


    #verso sotto
    cont = 1
    for i in range(x, len(griglia)):
        if (i < len(griglia)-1) and griglia[i+1][y] != 0 and  griglia[i][y] == griglia[i+1][y]:
            cont += 1
        else:
            nuova_x = i
            break
    if cont >= 4:
        return True
    
    #verso sopra
    cont = 1
    for i in range(nuova_x, -1, -1):
        if (i > 0) and griglia[i-1][y] != 0 and griglia[i][y] == griglia[i-1][y]:
            cont += 1
        else:
            break
    if cont >= 4:
        return True
    
    #verso destra
    cont = 1
    for i in range(y, len(griglia)):
        if (i < len(griglia)-1) and griglia[x][i+1] != 0 and griglia[x][i] == griglia[x][i+1]:
            cont += 1
        else:
            nuova_y = i
            break
    if cont >= 4:
        return True
    
    #verso sinistra
    cont = 1
    for i in range(nuova_y, -1, -1):
        if (i > 0) and griglia[x][i-1] != 0 and griglia[x][i] == griglia[x][i-1]:
            cont += 1
        else:
            break
    if cont >= 4:
        return True

    return False

def modifica(x, y, griglia, n_input):
    if (x >= 0 and x < len(griglia)) and (y >= 0 and y < len(griglia)):
        if griglia[x][y] == 0:
            simbolo = input('Quale simbolo vuoi utilizzare X o O?: ')
            while simbolo != 'O' and simbolo != 'X':
                simbolo = input('Quale simbolo vuoi utilizzare X o O?: ')
            
            if simbolo == 'X':
                griglia[x][y] = 1
            else:
                griglia[x][y] = 2
            return griglia, n_input-1
        
        else:
            print('La casella è occupata')
            return griglia, n_input
    else:
        print('Scegli una riga o una colonna diversa')
        return griglia, n_input

def gioca(griglia, sconfitta, n_input):
    stampa(griglia)
    x = int(input('Inserisci la riga: '))
    y = int(input('Inserisci la colonna: '))
    griglia, n_input = modifica(x, y, griglia, n_input)
    sconfitta = controllo(x, y, griglia)
    if sconfitta:
        print('Hai Perso!')
    elif n_input <= 0:
        print('Hai Vinto!')
    else:
        return gioca(griglia, False, n_input)

def controllo_iniziale(griglia):
    n_input = 0
    for i in range(len(griglia)):
        for j in range(len(griglia)):
            if griglia[i][j] == 0:
                n_input += 1
            if controllo(i, j, griglia):
                return False, None
    return True, n_input

def main():
    n = int(input('Inserisci la dimensione della griglia: '))
    griglia = [[randint(0, 2) for j in range(n)] for i in range(n)]
    check = controllo_facile(griglia)
    while not(check):
        griglia = [[randint(0, 2) for j in range(n)] for i in range(n)]
        check = controllo_facile(griglia)
    
    n_input = 0
    for i in range(len(griglia)):
        for j in range(len(griglia)):
            if griglia[i][j] == 0:
                n_input += 1
    
    gioca(griglia, False, n_input)
main()