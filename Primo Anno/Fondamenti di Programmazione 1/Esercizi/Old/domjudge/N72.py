def main():
    soluzione = list(input())
    archivio = []
    archivio = registra_matricola(archivio, 0, soluzione)
    stampa(archivio)

def registra_matricola(archivio, i, soluzione):
    Numero_Matricole = 90
    Matricola = []
    if i < Numero_Matricole:
        numero_matricola = input()
        Matricola.append(numero_matricola)
        registra_risposta(Matricola, soluzione)
        archivio.append(Matricola)
        return registra_matricola(archivio, i+1, soluzione)
    if i >= 3:
        return archivio

def registra_risposta(Matricola, soluzione):
    risposta = list(input())
    Matricola.append(risposta)
    punteggio = calcolo_punteggio(soluzione, risposta)
    Matricola.append(punteggio)
    return Matricola

def calcolo_punteggio(soluzione, risposta):
    punteggio = 0
    for i in range(len(soluzione)):
        if risposta[i] == 'X':
            punteggio += 0
        elif soluzione[i] == risposta[i]:
            punteggio += 2
        else:
            punteggio -= 1
    return punteggio
              
def stampa(archivio):
    for i in range (len(archivio)):
        print(archivio[i][0], end=' ')
        print(archivio[i][2])

main()