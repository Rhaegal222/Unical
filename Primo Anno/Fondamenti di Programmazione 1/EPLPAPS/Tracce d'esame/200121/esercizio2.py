def main():
    estratti = inserimento([])
    giocati = inserimento([])
    combo = scan(estratti, giocati, [[], []], 1)
    risultato(combo, combo[0])

def inserimento(numeri):
    for i in range(10):
        numeri.append(int(input()))
    return numeri

def scan(estratti, giocati, combo, cont):
    for i in giocati:
        if i in estratti:
            combo[cont].append(i)
        else:
            if len(combo[cont]) > 0:
                cont += 1
                combo.append([])
            combo[0].append(i)
    combo.pop(0)
    return combo

def risultato(combo, temp):
    for i in combo:
        if len(i) > len(temp):
            temp = i
    
    if len(temp) > 1 and len(temp) < 6:
        print(len(temp), end='')
    else:
        print(0, end='')
main()