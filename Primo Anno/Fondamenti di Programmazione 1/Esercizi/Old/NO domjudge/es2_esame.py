def main():
    numeri_giocati = inserisci_numeri_giocati([], 0)
    numeri_estratti = inserisci_numeri_estratti([], 0)
    risultato = controlla_numeri(numeri_giocati, numeri_estratti, 0, 0, 0)
    vincita(risultato)

def inserisci_numeri_giocati(numeri_giocati, i):
    if i > 9:
        return numeri_giocati
    else:
        numeri_giocati.append(int(input()))
        return inserisci_numeri_giocati(numeri_giocati, i+1)

def inserisci_numeri_estratti(numeri_estratti, i):
    if i > 9:
        return numeri_estratti
    else:
        numeri_estratti.append(int(input()))
        return inserisci_numeri_estratti(numeri_estratti, i+1)

def controlla_numeri(numeri_giocati, numeri_estratti, i, contatore, risultato):
    if i > 9:
        return risultato
    if numeri_giocati[i] in numeri_estratti:
        return controlla_numeri(numeri_giocati, numeri_estratti, i+1, contatore+1, risultato)
    else:
        if risultato < contatore:
            return controlla_numeri(numeri_giocati, numeri_estratti, i+1, 0, contatore)
        else:
            return controlla_numeri(numeri_giocati, numeri_estratti, i+1, 0, risultato)

def vincita(risultato):
    if risultato > 1 and risultato <= 5:
        print(risultato, end='')
    else:
        print(0, end='')

main()