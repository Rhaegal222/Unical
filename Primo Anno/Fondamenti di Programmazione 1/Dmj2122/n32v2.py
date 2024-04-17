def main():
    sequenza = inserimento([], int(input()))
    print('SI' if scan(sequenza, True, False) else 'NO', end='')

def inserimento(lista, x):
    while x != 0:
        lista.append(x)
        x = int(input())
    return lista

def scan(sequenza, crescente, decrescente):
    if len(sequenza) < 3:
            return False
    for i in range(len(sequenza)-1):
        if decrescente and not(crescente):
            if sequenza[i] >= sequenza[i+1]:
                crescente = True
        elif crescente and not(decrescente):
            if sequenza[i] >= sequenza[i+1]:
                decrescente = True
                crescente = False
    return (True if not(crescente) and decrescente else False)
            
main()