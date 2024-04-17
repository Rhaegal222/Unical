def main():
    comandi = inserimento([], int(input()))
    esecuzione(comandi, crea([]), 0, 0, True)

def inserimento(comandi, comando):
    while comando != 9:
        comandi.append(comando)
        comando = int(input())
    comandi.append(comando)
    return comandi   

def crea(matrice):
    for i in range(20):
        matrice.append([])
        for j in range(20):
            matrice[i].append(0)
    return matrice

def esecuzione(comandi, matrice, x_point, y_point, penna):
    for i in comandi:
        if i == 1:
            if penna:
                penna = False
        elif i == 2:
            if not(penna):
                penna = True
        elif i == 3:
            matrice, x_point = est(matrice, x_point, y_point, penna)
        elif i == 4:
            matrice, x_point = ovest(matrice, x_point, y_point, penna)
        elif i == 5:
            matrice, y_point = sud(matrice, x_point, y_point, penna)
        elif i == 6:
            matrice, y_point = nord(matrice, x_point, y_point, penna)
        elif i == 7:
            visualizza_pavimento(matrice)
        elif i == 8:
            continue
        elif i == 9:
            break
    return matrice

def nord(matrice, x_point, y_point, penna):
    passi = int(input('passi?'))
    print()
    for i in range(y_point-1, y_point-passi-1, -1):
        if y_point == 0:
            return matrice, y_point
        else:
            if penna:
                matrice[i][x_point] = 1
            y_point -= 1
    return matrice, y_point

def sud(matrice, x_point, y_point, penna):
    passi = int(input('passi?'))
    print()
    for i in range(y_point+1, y_point+passi+1):
        if y_point == 20:
            return matrice, y_point
        else:
            if penna:
                matrice[i][x_point] = 1
            y_point += 1
    return matrice, y_point
    
def est(matrice, x_point, y_point, penna):
    passi = int(input('passi?'))
    print()
    for i in range(x_point+1, x_point+passi+1):
        if x_point == 20:
            return matrice, x_point
        else:
            if penna:
                matrice[y_point][i] = 1
            x_point += 1
    return matrice, x_point

def ovest(matrice, x_point, y_point, penna):
    passi = int(input('passi?'))
    print()
    for i in range(x_point-1, x_point-passi-1, -1):
        if x_point == 0:
            return matrice, x_point
        else:
            if penna:
                matrice[y_point][i] = 1
            x_point -= 1
    return matrice, x_point

def visualizza_pavimento(matrice):
    for i in range(20):
        for j in range(20):
            if matrice[i][j] == 0:
                print(' ', end='')
            else:
                print('*', end='')
        print()
    return matrice

main()