def main():
    votazioni = [[],[],[]]
    votazioni = inserimento(votazioni)
    stampa(votazioni)

def inserimento(votazioni):
    x = int(input())
    if x == 0:
        return votazioni
    elif x == 1:
        votazioni[0].append(x)
        return inserimento(votazioni)
    elif x == 2:
        votazioni[1].append(x)
        return inserimento(votazioni)
    elif x == 3:
        votazioni[2].append(x)
        return inserimento(votazioni)

def stampa(votazioni):
    percentuale, tvoti = cpercentuale(votazioni)
    lesito = []
    bvotazione = 0
    esito = 0
    if tvoti > 0:
        for i in range(3):
            print(i+1, len(votazioni[i]), round(percentuale[i], 1))
            lesito.append(len(votazioni[i]))

            if len(votazioni[i]) > bvotazione:
                bvotazione = len(votazioni[i])
                esito = i
    if lesito.count(bvotazione) > 1 or bvotazione < tvoti/2 or tvoti == 0:
        print('BALLOTTAGIO', end='')
    else:
        print('VINCE', esito+1, end='')
        
def cpercentuale(votazioni):
    lista = []
    tvoti = 0
    for i in range(3):
        tvoti += len(votazioni[i])
    if tvoti > 0:
        for i in range(3):
            x = (len(votazioni[i])*100)/tvoti
            lista.append(x)

    return lista, tvoti
main()
