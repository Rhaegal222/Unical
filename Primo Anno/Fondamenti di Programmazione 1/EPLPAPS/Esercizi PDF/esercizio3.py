def main():
    n_squadre = int(input('Quante squadre giocano nel torneo?: '))
    tabellone = [[input() for j in range(n_squadre)] for i in range(n_squadre)]
    punti, bic, pia, mia = calcolo(tabellone, 1)
    dati = ordina(punti)
    statistiche(dati, bic, pia, mia)
    
def statistiche(dati, bic, pia, mia):
    print('Squadra con il maggior numero di vittorie in casa:', bic)
    print('Squadra con il maggior numero di vittorie in assoluto:', mia)
    print('Squadra che ha vinto il campionato:', dati[0][0])
    print('Squadra che é arrivata ultima nel torneo:', dati[0][len(dati[0])-1])
    print('Squadra che ha perse tutte le partite del torneo:', pia)
    print()
    stampa(dati)

def stampa(dati):
    print('CLASSIFICA COMPLETA')
    for i in range(1, len(dati)):
        print(str(i)+')', dati[0][i-1], 'Punti:', sum(dati[i]))

def ordina(punti):
    for i in range(1, len(punti)):
        for j in range(1, len(punti)):
            if sum(punti[i]) > sum(punti[j]) and i != j:
                punti[i], punti[j] = punti[j], punti[i]
                punti[0][i-1], punti[0][j-1] = punti[0][j-1], punti[0][i-1]
    return punti

def src_pia(punti):
    pia = -1
    for i in range(1, len(punti)):
        if sum(punti[i]) == 0:
            pia = punti[0][i-1]
            return pia
    return 'NESSUNA'

def punti_ritorno(ritorno, tabellone, punti, puntatore, vinte):
    ritorno = [[tabellone[j][i] for j in range(len(tabellone))] for i in range(len(tabellone))]
    for i in ritorno:
        punti[puntatore].append((i.count('2'))*3)
        vinte[puntatore-1] += (i.count('2'))
        punti[puntatore].append((i.count('0'))*1)
        puntatore+=1
    return punti, vinte

def src_bic(vinte, indice):
    for i in vinte:
        if i > vinte[indice]:
            indice = vinte.index(i)
    return indice

def punti_andata(tabellone, puntatore):
    punti = [[] for i in range(len(tabellone)+1)]
    bic = []
    for i in tabellone:
        punti[0].append('S'+str(puntatore))
        punti[puntatore].append((i.count('1'))*3)
        bic.append(i.count('1'))
        punti[puntatore].append((i.count('0'))*1)
        puntatore+=1
    return punti, bic

def src_mia(vinte, indice):
    for i in vinte:
        if i > vinte[indice]:
            indice = vinte.index(i)
    return indice

def calcolo(tabellone, puntatore):
    punti, vinte = punti_andata(tabellone, puntatore)
    bic = punti[0][src_bic(vinte, 0)]
    punti, vinte = punti_ritorno([], tabellone, punti, puntatore, vinte)
    mia = punti[0][src_mia(vinte, 0)]
    pia = src_pia(punti)
    return punti, bic, pia, mia

main()