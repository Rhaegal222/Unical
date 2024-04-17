def inserisci_peso_quesito():
    pesi_quesiti = []
    for i in range(8):
        pesi_quesiti.append(int(input()))
    return pesi_quesiti

def inserisci_studente(pesi_quesiti):
    lista_studenti = []
    for i in range(70):
        lista_studenti.append(studente(pesi_quesiti))
    return lista_studenti

def studente(pesi_quesiti):
    libretto = []
    libretto.append(input())
    libretto = punti_studente(libretto, pesi_quesiti)
    return libretto

def punti_studente(libretto, pesi_quesiti):
    for i in range(8):
        libretto.append(int(input()))
    calcolo_voto(libretto, pesi_quesiti)
    return libretto

def calcolo_voto(libretto, pesi_quesiti):
    Somma = 0
    for i in range(1, len(libretto)):
        Somma = Somma + libretto[i] * pesi_quesiti[i - 1]
    libretto.append(Somma)
    return libretto

def stampa(lista_studenti, voto_di_soglia):
    lista_di_stampa = []
    for i in range(len(lista_studenti)):
        if lista_studenti[i][9] >= voto_di_soglia:
            lista_di_stampa.append([lista_studenti[i][0], lista_studenti[i][9]])
    for i in range(len(lista_di_stampa)):
        print(lista_di_stampa[i][0], lista_di_stampa[i][1], end='')
        print()
    best = migliore(lista_di_stampa)
    worst = peggiore(lista_di_stampa)
    print(len(lista_di_stampa), best, worst, end='')

def migliore(lista_di_stampa):
    for i in range(len(lista_di_stampa)):
        for j in range(len(lista_di_stampa)-1):
            if (lista_di_stampa[j][1]) < (lista_di_stampa[j+1][1]):
                temp=lista_di_stampa[j]
                lista_di_stampa[j]=lista_di_stampa[j+1]
                lista_di_stampa[j+1]=temp
    best = (lista_di_stampa[0][0])
    return best    

def peggiore(lista_di_stampa):
    for i in range(len(lista_di_stampa)):
        for j in range(len(lista_di_stampa)-1):
            if (lista_di_stampa[j][1]) > (lista_di_stampa[j+1][1]):
                temp=lista_di_stampa[j]
                lista_di_stampa[j]=lista_di_stampa[j+1]
                lista_di_stampa[j+1]=temp
    worst = (lista_di_stampa[0][0])
    return worst

def main():
    pesi_quesiti = inserisci_peso_quesito()
    lista_studenti = inserisci_studente(pesi_quesiti)
    voto_di_soglia = int(input())
    stampa(lista_studenti, voto_di_soglia)

main()

