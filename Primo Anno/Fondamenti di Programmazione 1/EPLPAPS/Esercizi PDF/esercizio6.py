from random import randint
#--------------------------------------------------Funzioni Debbugging--------------------------------------------------#
def stampa(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j], end='')
        print()
    print()

#--------------------------------------------------Funzioni BOT / Giocatore---------------------------------------------#
def crea():
    tabella1 = [[0 for j in range(10)] for i in range(10)]
    tabella2 = [[0 for j in range(10)] for i in range(10)]
    tabelle = [tabella1, tabella2]
    return tabelle

def ch_ctrl_per(x, y, tabella1):
    if tabella1[x][y] != 0: #cella
        return False
    if (x < len(tabella1)-1 and y > 0) and tabella1[x+1][y-1] != 0: #riga sotto - colonna sinistra
        return False
    if x < len(tabella1)-1 and tabella1[x+1][y] != 0: #riga sotto - colonna
        return False
    if (x < len(tabella1)-1 and y < len(tabella1)-1) and tabella1[x+1][y+1] != 0: #riga sotto - colonna destra
        return False
    if (x > 0 and y > 0) and tabella1[x-1][y-1] != 0: #riga sopra - colonna sinistra 
        return False
    if x > 0 and tabella1[x-1][y] != 0: #riga sopra - colonna
        return False
    if( x > 0 and y < len(tabella1)-1) and tabella1[x-1][y+1] != 0: #riga sopra - colonna destra
        return False
    if y > 0 and tabella1[x][y-1] != 0: #riga - colonna sinistra
        return False
    if y < len(tabella1)-1 and tabella1[x][y+1] != 0: #riga - colonna destra
        return False
    return True

def ctr_nord(x, y, nave, navi, tabella1):
    dim_nave = (navi.index(nave))+1
    if (x < len(tabella1)-1 and y > 0) and tabella1[x+1][y-1] != 0:
        return False
    if x < len(tabella1)-1 and tabella1[x+1][y] != 0:
        return False
    if (x < len(tabella1)-1 and y < len(tabella1)-1) and tabella1[x+1][y+1] != 0:
        return False
    for i in range(x, (x-dim_nave), -1):
        if i < 0 or (y > 0 and tabella1[i][y-1] != 0):
            return False
        if i < 0 or tabella1[i][y] != 0:
            return False
        if i < 0 or (y < len(tabella1)-1 and tabella1[i][y+1] != 0):
            return False
    if (i > 0 and y > 0) and tabella1[i-1][y-1] != 0:
        return False
    if i > 0 and tabella1[i-1][y] != 0:
        return False
    if (i > 0 and y < len(tabella1)-1) and tabella1[i-1][y+1] != 0:
        return False
    return True

def ctr_sud(x, y, nave, navi, tabella1):
    dim_nave = (navi.index(nave))+1
    if (x > 0 and y > 0) and tabella1[x-1][y-1] != 0:
        return False
    if x > 0 and tabella1[x-1][y] != 0:
        return False
    if( x > 0 and y < len(tabella1)-1) and tabella1[x-1][y+1] != 0:
        return False
    for i in range(x, (x+dim_nave)):
        if i >= len(tabella1) or (tabella1[i][y-1] != 0 and y > 0):
            return False
        if i >= len(tabella1) or tabella1[i][y] != 0:
            return False
        if i >= len(tabella1) or ( y < len(tabella1)-1 and tabella1[i][y+1] != 0):
            return False
    if (i < len(tabella1)-1 and y > 0) and tabella1[i+1][y-1] != 0:
        return False
    if i < len(tabella1)-1 and tabella1[i+1][y] != 0:
        return False
    if (i < len(tabella1)-1 and y < len(tabella1)-1) and tabella1[i+1][y+1] != 0:
        return False
    return True

def ctr_est(x, y, nave, navi, tabella1):
    dim_nave = (navi.index(nave))+1
    if (x > 0 and y > 0) and tabella1[x-1][y-1] != 0:
        return False
    if y > 0 and tabella1[x][y-1] != 0:
        return False
    if (x < len(tabella1)-1 and y > 0) and tabella1[x+1][y-1] != 0:
        return False
    for i in range(y, (y+dim_nave)):
        if i >= len(tabella1) or tabella1[x][i] != 0:
            return False
        if i >= len(tabella1) or tabella1[x][i] != 0:
            return False
        if i >= len(tabella1) or tabella1[x][i] != 0:
            return False
    if (x > 0 and i < len(tabella1)-1) and tabella1[x-1][i+1] != 0:
        return False
    if i < len(tabella1)-1 and tabella1[x][i+1] != 0:
        return False
    if (x < len(tabella1)-1 and i < len(tabella1)-1) and tabella1[x+1][i+1] != 0:
        return False
    return True

def ctr_ovest(x, y, nave, navi, tabella1):
    dim_nave = (navi.index(nave))+1
    if (x > 0 and y < len(tabella1)-1) and tabella1[x-1][y+1] != 0:
        return False
    if y < len(tabella1)-1 and tabella1[x][y+1] != 0:
        return False
    if (x < len(tabella1)-1 and y < len(tabella1)-1) and tabella1[x+1][y+1] != 0:
        return False
    for i in range(y, (y-dim_nave), -1):
        if i < 0 or tabella1[x][i] != 0:
            return False
    if (x > 0 and i > 0) and tabella1[x-1][i-1] != 0:
        return False
    if i > 0 and tabella1[x][i-1] != 0:
        return False
    if (x < len(tabella1)-1 and i > 0) and tabella1[x+1][i-1] != 0:
        return False
    return True

def aggiungi_nave(tabella1, x, y, nave, navi, cont_navi, direzione):
    dim_nave = (navi.index(nave))+1 
    if direzione == 'nord' or direzione == '1':
        for i in range(x, (x-dim_nave), -1):
            tabella1[i][y] = dim_nave
    elif direzione == 'sud' or direzione == '2':
        for i in range(x, x+dim_nave):
            tabella1[i][y] = dim_nave
    elif direzione == 'est' or direzione == '3':
        for i in range(y,  y+dim_nave):
            tabella1[x][i] = dim_nave
    elif direzione == 'ovest' or direzione == '4':
        for i in range(y, (y-dim_nave), -1):
            tabella1[x][i] = dim_nave
    else:
        print("C'é qualcosa non va")
    cont_navi[navi.index(nave)] -=1

def colpisci(turn_player, turn_computer, player, computer, x, y, point_pla, point_cmp, navi):
    if turn_player:
        turn_player, point_pla = aim(computer[0], player[1], x, y, point_pla, navi)
        if turn_player:
            return True, False, point_pla, point_cmp
        else:
            return False, True, point_pla, point_cmp
    if turn_computer:
        turn_computer, point_cmp = aim(player[0], computer[1], x, y, point_cmp, navi)
        if turn_computer:
            return False, True, point_pla, point_cmp 
        else:
            return True, False, point_pla, point_cmp

def aim(avversario, riferimento, x, y, point, navi):
    if avversario[x][y] == '*':
        print('Casella giá colpita')
        return True, point
    elif avversario[x][y] != 0:
        nave = avversario[x][y]
        avversario[x][y] = '*'
        riferimento[x][y] = '*'
        affondato(x, y, navi, nave, avversario)
        point += 1
        return True, point
    else:
        avversario[x][y] = '_'
        riferimento[x][y] = '_'
        return False, point

def affondato(x, y, navi, dim_nave, tabella):
    nave = navi[dim_nave-1]
    ship = 0
    if dim_nave == 1:
        print('Affondato', nave)
        return

    for i in range(x, (x-dim_nave), -1):
        if i < 0 or tabella[i][y] == 0:
            break

#--------------------------------------------------Funzioni Giocatore----------------------------------------------------#
def inserisci(tabella1, navi, cont_navi):
    while sum(cont_navi) > 0:
        x, y = iniziale()
        nave = controllo_nave(navi, cont_navi)
        dim_nave = (navi.index(nave))+1
        if dim_nave > 1:
            direzioni = dir_disponibili(x, y, nave, navi, tabella1)
            if len(direzioni)>0:
                direzione = controllo_posizione(direzioni)
                aggiungi_nave(tabella1, x, y, nave, navi, cont_navi, direzione)
                print('Nave inserita correttamente')
                stampa(tabella1)
        elif dim_nave == 1:
            ctrl_per = ch_ctrl_per(x, y, tabella1)
            if ctrl_per:
                tabella1[x][y] = (navi.index(nave))+1
                cont_navi[navi.index(nave)] -= 1
            else:
                print("Casella occupata da un'altra nave, scegli un'altra casella")
                return inserisci(tabella1, navi, cont_navi)
        else:
            return inserisci(tabella1, navi, cont_navi)
    print('Tutte le navi sono state inserite correttamente!')
    print('Il computer sta schierando le sue navi!')

def iniziale():
    x = input('Inserisci la riga della casella di partenza (da 0 a 9)): ')
    while not(x.isdigit()) or (int(x) > 9 or int(x) < 0):
        x = input('Inserisci la riga della casella di partenza (da 0 a 9): ')
    y = input('Inserisci la colonna della casella di partenza (da 0 a 9): ')
    while not(y.isdigit()) or (int(y) > 9 or int(y) < 0):
        y = input('Inserisci la colonna della casella di partenza (da 0 a 9): ')
    conf = input("Inserisci y per confermare x per ripetere la scelta: ")
    
    if conf == 'y': 
        conf = True
    else:
        conf = False
    
    if conf:
        return int(x), int(y)
    else:
        return iniziale()

def controllo_nave(navi, cont_navi):
    navi_disponibili(navi, cont_navi)
    nave = input('Inserisci il nome della nave che vuoi inserire o la sua grandezza (0 per ripetere la scelta): ')
    if nave == '1': nave = 'sommergibile'
    elif nave == '2': nave = 'vedetta'
    elif nave == '3': nave = 'incrociatori'
    elif nave == '4': nave = 'portaerei'
    elif nave == '0': return controllo_nave(navi, cont_navi)

    if nave not in navi:
        print('Nave non esistente, inserisci il nome corretto')
        return controllo_nave(navi, cont_navi)
    elif cont_navi[navi.index(nave)] == 0:
        print("Tipologia di nave esaurita, scegli un'altra nave: ")
        return controllo_nave(navi, cont_navi)
    else:
        print('Nave selezionata correttamente')
        return nave

def dir_disponibili(x, y, nave, navi, tabella1): 
    verso = ['nord', 'sud', 'est', 'ovest']
    
    nord = ctr_nord(x, y, nave, navi, tabella1)
    sud = ctr_sud(x, y, nave, navi, tabella1)
    est = ctr_est(x, y, nave, navi, tabella1)
    ovest = ctr_ovest(x, y, nave, navi, tabella1)

    direzioni = [nord, sud, est, ovest]
    cancellati = 0

    for i in range(len(direzioni)):
        if not(direzioni[i]) and len(verso) > 0:
            verso.pop(i - cancellati)
            cancellati += 1
    
    if len(verso) > 2:
        print('Puoi posizionare la nave verso: ', end='')
        for i in range(len(verso)-2):
            print(verso[i]+',', end=' ')
        print(verso[i+1], 'o', end=' ')
        print(verso[i+2]+'.')
    elif len(verso) == 2:
        print('Puoi posizionare la nave verso: ', end='')
        print(verso[0], 'o', verso[1])
    elif len(verso) == 1:
        print('Puoi posizionare la nave verso: ', end='')
        print(verso[0])
    else:
        print("Non puoi posizionare la nave in nessuna direzione, scegli una nuova posizione o un'altra nave")
    
    return verso

def controllo_posizione(direzioni):
    direzione = input('Scegliere una direzione verso il quale posizionare una nave: ')
    if direzione not in direzioni:
        print('Direzione non ammessa, inserire una direzione valida')
        return controllo_posizione(direzioni)
    print('Direzione inserita correttamente!')
    return direzione

def navi_disponibili(navi, cont_navi):
    print('Numero di navi disponibili: ')
    for i in range(len(navi)):
        print(navi[i]+':', cont_navi[i])

#--------------------------------------------------Funzioni Computer-----------------------------------------------------#
def npc_insert(tabella1, navi, cont_navi):
    while sum(cont_navi) > 0:
        x, y = randint(0, 9), randint(0, 9)
        nave = controllo_nave_npc(navi, cont_navi)
        dim_nave = (navi.index(nave))+1
        if dim_nave > 1:
            direzioni = dir_disponibili_npc(x, y, nave, navi, tabella1)
            if len(direzioni)>0:
                direzione = direzioni[randint(0, len(direzioni)-1)]
                aggiungi_nave(tabella1, x, y, nave, navi, cont_navi, direzione)
        elif dim_nave == 1:
            ctrl_per = ch_ctrl_per(x, y, tabella1)
            if ctrl_per:
                tabella1[x][y] = (navi.index(nave))+1
                cont_navi[navi.index(nave)] -= 1
            else:
                return npc_insert(tabella1, navi, cont_navi)
        else:
            return npc_insert(tabella1, navi, cont_navi)

def controllo_nave_npc(navi, cont_navi):
    nave = navi[randint(0, 3)]
    if cont_navi[navi.index(nave)] == 0:
        return controllo_nave_npc(navi, cont_navi)
    else:
        return nave

def dir_disponibili_npc(x, y, nave, navi, tabella1):
    verso = ['nord', 'sud', 'est', 'ovest']

    nord = ctr_nord(x, y, nave, navi, tabella1)
    sud = ctr_sud(x, y, nave, navi, tabella1)
    est = ctr_est(x, y, nave, navi, tabella1)
    ovest = ctr_ovest(x, y, nave, navi, tabella1)
    
    direzioni = [nord, sud, est, ovest]
    cancellati = 0
    
    for i in range(len(direzioni)):
        if not(direzioni[i]) and len(verso) > 0:
            verso.pop(i - cancellati)
            cancellati += 1    
    return verso

#--------------------------------------------------Partita---------------------------------------------------------------#
def stampa_tabelle(player):
    for i in range(len(player[0])):
        for j in range(len(player[0])+len(player[0])+1):
            if j == len(player[0]):
                print(' ', end='')
            elif j < len(player[1]):
                print(player[0][i][j] , end='')
            else:
                print(player[1][i][j-1-(len(player[1]))] , end='')
        print()

def testa_o_croce():
    moneta = ['testa', 'croce']
    x = randint(0, 1)
    if x == 0:
        cmp_cho = randint(0, 1)
        if cmp_cho == 0:
            pla_cho = 1
        else:
            pla_cho = 0
        print('Il computer ha scelto:', moneta[cmp_cho])
    else:
        pla_cho = input('Scegli la faccia della moneta 0 per testa, 1 per croce: ')
        while pla_cho != '1' and pla_cho != '0':
            pla_cho = input('Scegli la faccia della moneta 0: testa, 1: croce')
        print('Hai scelto:', moneta[int(pla_cho)])
        
        pla_cho = int(pla_cho)
        if pla_cho == 0:
            cmp_cho = 1
        else:
            cmp_cho = 0

    if randint(0, 1) == cmp_cho:
        print('Inizia il computer')
        return False, True
    else:
        print('Inizi Tu!')
        return True, False

def inserisci_coordinate(turn_player, turn_computer):
    if turn_player:
        x = input('Inserisci la riga della casella che vuoi colpire (da 0 a 9)): ')
        while not(x.isdigit()) or (int(x) > 9 or int(x) < 0):
                x = input('Inserisci la riga della casella che vuoi colpire (da 0 a 9)): ')
        y = input('Inserisci la colonna della casella che vuoi colpire (da 0 a 9)): ')
        while not(y.isdigit()) or (int(y) > 9 or int(y) < 0):
                y = input('Inserisci la colonna della casella che vuoi colpire (da 0 a 9)): ')
    elif turn_computer:
        x, y = randint(0, 9), randint(0, 9)
    return int(x), int(y)

def start(player, computer, navi):
    stampa_tabelle(player)
    turn_player, turn_computer = testa_o_croce()
    point_pla, point_cmp = 0, 0
    while point_pla < 20 and point_cmp < 20:
        if turn_player:
            x, y, = inserisci_coordinate(turn_player, turn_computer)
            print('Hai scelto di colpire nel punto:', '('+str(x)+', '+str(y)+')')
            turn_player, turn_computer, point_pla, point_cmp = colpisci(turn_player, turn_computer, player, computer, x, y, point_pla, point_cmp, navi)
            stampa_tabelle(player)
        elif turn_computer:
            x, y = inserisci_coordinate(turn_player, turn_computer)
            print('Il computer colpisce nel punto:', '('+str(x)+', '+str(y)+')')
            turn_player, turn_computer, point_pla, point_cmp = colpisci(turn_player, turn_computer, player, computer, x, y, point_pla, point_cmp, navi)
        else:
            "C'é qualcosa che non quadra"
    if point_cmp > 20:
        print('Ha vinto il computer')
    else:
        print('Hai vinto tu!')
    print('Computer:', point_cmp, '- Player:', point_pla)

#--------------------------------------------------Main------------------------------------------------------------------#
def main():
    navi = ['sommergibile', 'vedetta', 'incrociatori', 'portaerei']
    cont_navi = [4, 3, 2, 1]
    #player, computer = crea(), crea()
    player = crea()
    computer = [[list('2000000333'),list('2030000000'),list('0030444400'),list('0030000000'),list('0000000000'),list('0003010002'),list('0003000002'),list('0203000100'),list('0200000000'),list('0000001001')], [[0 for j in range(10)] for i in range(10)]]
    for i in range(len(computer[0])):
        computer[0][i] = list(map(int, computer[0][i]))
    inserisci(player[0], navi, cont_navi.copy())
    #npc_insert(computer[0], navi, cont_navi.copy())
    print(computer[0])
    start(player, computer, navi)

main()