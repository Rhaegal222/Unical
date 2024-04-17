def main():
    sequenza = inserimento(int(input()), [])
    print('SI' if scan(sequenza, True, False) and len(sequenza) > 2 else 'NO', end='')

def inserimento(x, sequenza):
    while x != 0:
        sequenza.append(x)
        x = int(input())
    return sequenza

def scan(sequenza, crescente, decrescente):
    for i in range(len(sequenza)-1):
        if decrescente and not(crescente):
            if sequenza[i] >= sequenza[i+1]:
                crescente = True
        elif crescente and not(decrescente):
            if sequenza[i] >= sequenza[i+1]:
                decrescente = True
                crescente = False
    return(True if not(crescente) and decrescente else False)

main()