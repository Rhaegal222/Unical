def main():
    sequenza = inserimento([])
    compresi, non_compresi = scan(sequenza, [], [])
    stampa(compresi, non_compresi)

def scan(sequenza, non_compresi, compresi):
    for i in sequenza:
        if i < - 50 or i > 50:
            non_compresi.append(i)
        elif i >= - 50 or i <= 50:
            compresi.append(i)
    return compresi, non_compresi

def inserimento(sequenza):
    for i in range(100):
        sequenza.append(int(input()))
    return sequenza
    
def stampa(compresi, non_compresi):
    if len(non_compresi) > 0:
        for i in non_compresi:
            print(i, end='')
    else:
        print('VUOTO1', end='')
    print()
    if len(compresi) > 0:
        print(round(sum(compresi)/len(compresi), 6), end='')
    else:
        print('VUOTO2', end='')
main()