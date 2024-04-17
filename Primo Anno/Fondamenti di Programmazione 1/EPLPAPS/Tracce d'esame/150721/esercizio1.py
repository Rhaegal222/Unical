from random import randint
def main():
    numero_clienti = int(input())
    db_clienti = [[input() for j in range(3)] for i in range(numero_clienti)]
    clienti_da_rimuovere = [[input(), input()] for i in range(numero_clienti)]
    numero_nuovi_clienti = int(input())
    db_nuovi_clienti = [[input() for j in range(3)] for i in range(numero_nuovi_clienti)]
    db_clienti = delete(db_clienti, clienti_da_rimuovere)
    db_clienti = add(db_clienti, db_nuovi_clienti)
    casuale = gen([], db_clienti)
    coppie = matching(casuale, db_clienti, [])
    stampa(coppie)

def stampa(coppie):
    for i in coppie:
        for j in range(len(i)):
            if j < len(i)-1:
                print(i[j][1], i[j][2], 'anni e ', end='')
            else:
                print(i[j][1], i[j][2])

def matching(casuale, db_clienti, coppie):
    for i in range(len(casuale)//2):
        coppie.append([db_clienti[casuale[i]], db_clienti[casuale[len(casuale)-1-i]]])
    
    if len(casuale) % 2 != 0:
        solo = db_clienti[(len(casuale)//2)+1]
        dif = []
        
        for i in coppie:
            dif.append(int(solo[2]) - (int(i[0][2]) + int(i[1][2])) / 2)
        
        indice = 0
        for i in range(1, len(dif)):
            if dif[i] < dif[indice]:
                indice = i
        
        coppie[indice].append(db_clienti[casuale[(len(casuale)//2)]])
        return coppie

def gen(casuale, db_clienti):
    i = 0
    while i <= len(db_clienti)-1:
        x = randint(0, len(db_clienti)-1)
        if x not in casuale:
            casuale.append(x)
            i += 1
    return casuale

def add(db_clienti, db_nuovi_clienti):
    for i in db_nuovi_clienti:
        if i not in db_clienti:
            db_clienti.append(i)
    return db_clienti

def delete(db_clienti, clienti_da_rimuovere):
    for i in range(len(clienti_da_rimuovere)):
        for j in range(len(db_clienti)):
            if clienti_da_rimuovere[i][0] == db_clienti[j][0] and clienti_da_rimuovere[i][1] == 'NO':
                db_clienti[j] = [0, 0]
    for i in db_clienti:
        if i == [0, 0]:
            db_clienti.remove(i)
    return db_clienti

main()