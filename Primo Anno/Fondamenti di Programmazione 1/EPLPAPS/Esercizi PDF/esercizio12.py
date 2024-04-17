from random import randint
def src_mese(calendario, mese_mag, i):
    if i >= len(calendario):
        return mese_mag
    if sum(calendario[i]) > sum(calendario[mese_mag]):
        mese_mag = i
    return src_mese(calendario, mese_mag, i+1)

def spesa_fissa(giorno, calendario, i):
    if i >= len(calendario):
        return calendario[0][giorno]
    if calendario[i][giorno] != calendario[0][giorno]:
        return 'somme diverse'
    return spesa_fissa(giorno, calendario, i+1)

def cosa_strana(calendario, indice):
    if indice >= len(calendario):
        return False
    mese = calendario[indice]
    media = (sum(mese))/len(calendario[0])
    for i in range(2,len(mese)):
        if mese[i] != 0: 
            continue
        elif mese[i-2]+mese[i-1] > media and mese[i] == 0:
            return i
    return cosa_strana(calendario, indice+1) 

def main():
    mesi = ['Gennaio','Febbraio','Marzo','Aprile','Maggio','Giugno','Luglio','Agosto','Settembre','Ottobre','Novembre','Dicembre']
    #calendario = [[int(input()) for j in range(31)]for i in range(12)]
    calendario = [[randint(0, 100) for j in range(31)]for i in range(12)]
    for i in range(len(calendario)):
        for j in range(len(calendario[0])):
            print(calendario[i][j], end='')
        print()

    print('Ciccio ha speso di più in:', mesi[src_mese(calendario, 0, 1)])
    giorno = int(input())
    print('Nel giorno', giorno, 'Ciccio ha speso sempre:', spesa_fissa(giorno, calendario, 1),'euro')
    risultato = cosa_strana(calendario, 0)
    print('NO' if not(risultato) else risultato)
main()