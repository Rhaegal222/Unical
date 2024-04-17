def main():
    giocatore1, giocatore2 = Player()
    tabella = crea_tabella()
    partita(giocatore1, giocatore2, tabella, 0)

def Player():
    nome1 = (input('Inserisci il nome del primo giocatore: '))
    nome2 = (input('Inserisci il nome del secondo giocatore: '))
    giocatore1, giocatore2 = scegli_segno(nome1, nome2)
    stampa_scelte(giocatore1, giocatore2)
    return giocatore1, giocatore2

def scegli_segno(nome1, nome2):
    tupla = [1, 2]
    print(nome1, 'X o O?: ', end='')
    scelta = input()
    if scelta == 'X' or scelta == 'x':
        scelta = 0
        return [nome1, tupla[scelta]], [nome2, tupla[scelta+1]]
    elif scelta == 'O' or scelta == 'o':
        scelta = 1
        return [nome1, tupla[scelta]], [nome2, tupla[scelta-1]]
    else:
        print('Hai digitato un carattere non valido. Per favore riprova')
        return scegli_segno(nome1, nome2)

def stampa_scelte(giocatore1, giocatore2):
    print()
    print(giocatore1[0], 'ha scelto: ', 'X' if giocatore1[1] == 1 else 'O')
    print(giocatore2[0], 'ha scelto: ', 'X' if giocatore2[1] == 1 else 'O')
    print()

def inserisci_giocata(giocatore):
    print()
    print('Per giocare inserisci il numero della casella')
    print('Le caselle sono numerate da 1 a 9 partendo dalla prima in alto a sinistra: ', end='')
    giocata = int(input())
    return giocata

def partita(giocatore1, giocatore2, tabella, vincitore):
    if vincitore == 0:
        giocata1 = inserisci_giocata(giocatore1)
        giocatore1.append(giocata1)
        tabella = svolgimento(giocatore1, tabella)
    
    vincitore = cerca_il_vincitore(tabella)
    
    if vincitore == 0:
        giocata2 = inserisci_giocata(giocatore2)
        giocatore2.append(giocata2)
        tabella = svolgimento(giocatore2, tabella)

    vincitore = cerca_il_vincitore(tabella)

    if vincitore == 1:
        print('Vince X')
    elif vincitore == 2:
        print('Vince X')
    else:
        return partita(giocatore1, giocatore2, tabella, 0)
    
def cerca_il_vincitore(tabella):
    verifica = [[1, 1, 1], [2, 2, 2]]

    #diagonale principale
    test = []
    for i in range(len(tabella)):
        for j in range(len(tabella)):
            if i == j:
                test.append(tabella[i][j])
    if test == verifica[0]:
        return 1
    elif test == verifica[1]:
        return 2
    else:
        return 0

    #diagonale secondaria
    test = []
    for i in range(len(tabella)):
        test = []
        for j in range(tabella):
            if i + j == 2:
                test.append(tabella[i][j])
    if test == verifica[0]:
        return 1
    elif test == verifica[1]:
        return 2
    else:
        return 0
    
def svolgimento(giocatore, tabella):
    for i in range(len(tabella)):
        for j in range(len(tabella)):
            if tabella[i][j] == 0:
                if giocatore[len(giocatore)-1] == i*3+j+1:
                    tabella[i][j] = giocatore[1]
                if giocatore[len(giocatore)-1] == i*3+j+1:
                    tabella[i][j] = giocatore[1]                    
    stampa_tabella(tabella)
    return tabella

def crea_tabella():
    tabella = []
    for i in range(3):
        tabella.append([])
        for j in range(3):
            tabella[i].append(0)
    return tabella

def stampa_tabella(tabella):
    for i in range(len(tabella)):
        for j in range(len(tabella)):
            if tabella[i][j]== 0:
                print('| |', end='')
            if tabella[i][j]== 1:
                print('|X|', end='')
            if tabella[i][j]== 2:
                print('|O|', end='')
        print()

main()