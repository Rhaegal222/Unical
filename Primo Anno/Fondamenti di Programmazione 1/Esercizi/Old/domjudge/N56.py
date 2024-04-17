def main():
    pavimento = crea_matrice()
    lista_comandi = comandi_input()
    status_penna = True
    esecuzione_comandi(pavimento, lista_comandi, status_penna, 0, 0)

def crea_matrice():
    pavimento = []
    for i in range(20):
        pavimento.append([0]*20)
    return pavimento

def comandi_input():
    lista_comandi = []
    while True:
        i = int(input())
        if i == 9:
            lista_comandi.append(i)
            break
        else:
            lista_comandi.append(i)
    return lista_comandi

def esecuzione_comandi(pavimento, lista_comandi, status_penna, posizione_verticale, posizione_orizzontale):
    for i in lista_comandi:
        if i == 1:
            status_penna = penna(i)
        elif i == 2:
            status_penna = penna(i)
        elif i == 3:
            (pavimento, status_penna, posizione_orizzontale, posizione_verticale) = vai_ad_est(pavimento, status_penna, posizione_orizzontale, posizione_verticale)
        elif i == 4:
            (pavimento, status_penna, posizione_orizzontale, posizione_verticale) = vai_ad_ovest(pavimento, status_penna, posizione_orizzontale, posizione_verticale)
        elif i == 5:
            (pavimento, status_penna, posizione_orizzontale, posizione_verticale) = vai_a_sud(pavimento, status_penna, posizione_orizzontale, posizione_verticale)
        elif i == 6:
            (pavimento, status_penna, posizione_orizzontale, posizione_verticale) = vai_a_nord(pavimento, status_penna, posizione_orizzontale, posizione_verticale)
        elif i == 7:
            visualizza_pavimento(pavimento)
        elif i == 8:
            continue
        elif i == 9:
            break

def penna(i):
    status_penna = True
    if i == 1:
        status_penna = False
    else:
        status_penna = True
    return status_penna

def vai_ad_est(pavimento, status_penna, posizione_orizzontale, posizione_verticale):
    X = int(input("passi?"))
    print()
    if X >= 20:
        X = 19
    for i in range(posizione_orizzontale + 1, posizione_orizzontale + X + 1):
        if status_penna and i < 20 and i >= 0:
            pavimento[posizione_verticale][i] = 1
        else:
            if i >= 20:
                i = 19
        conta_posizione = i
    posizione_orizzontale = conta_posizione
    if posizione_orizzontale >= 20:
        posizione_orizzontale = 20
    return pavimento, status_penna, posizione_orizzontale, posizione_verticale

def vai_ad_ovest(pavimento, status_penna, posizione_orizzontale, posizione_verticale):
    X = int(input("passi?"))
    print()
    if X >= 20:
        X = 19
    for i in range(posizione_orizzontale - 1, posizione_orizzontale - X - 1, - 1):
        if status_penna and i < 20 and i >= 0:
            pavimento[posizione_verticale][i] = 1
        else:
            if i < 0:
                i = 0
        conta_posizione = i
    posizione_orizzontale = conta_posizione
    if posizione_orizzontale <= 0:
        posizione_orizzontale = 0
    return pavimento, status_penna, posizione_orizzontale, posizione_verticale

def vai_a_sud(pavimento, status_penna, posizione_orizzontale, posizione_verticale):
    X = int(input("passi?"))
    print()
    if X >= 20:
        X = 19
    for i in range(posizione_verticale + 1, posizione_verticale + X + 1):
        if status_penna and i < 20 and i >= 0:
            pavimento[i][posizione_orizzontale] = 1
        else:
            if i >= 20:
                i = 19
        conta_posizione = i
    posizione_verticale = conta_posizione 
    if posizione_verticale >= 20:
        posizione_verticale = 20
    return pavimento, status_penna, posizione_orizzontale, posizione_verticale

def vai_a_nord(pavimento, status_penna, posizione_orizzontale, posizione_verticale):
    X = int(input("passi?"))
    print()
    if X >= 20:
        X = 19
    for i in range(posizione_verticale - 1, posizione_verticale - X-1, -1):
        if status_penna and i < 20 and i >= 0:
            pavimento[i][posizione_orizzontale] = 1
        else:
            if i <= 0:
                i = 0
        conta_posizione = i
    posizione_verticale = conta_posizione
    if posizione_verticale <= 0:
        posizione_verticale = 0
    return pavimento, status_penna, posizione_orizzontale, posizione_verticale

def visualizza_pavimento(pavimento):
    for i in range(len(pavimento)):
        for j in range(len(pavimento)):
            if pavimento[i][j] == 1:
                print("|*|",end="")
            else:
                print("| |",end="")
        print()
main()