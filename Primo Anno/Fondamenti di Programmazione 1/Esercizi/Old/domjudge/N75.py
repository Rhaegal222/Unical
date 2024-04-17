def main():
    alfabeto = [chr(i) for i in range(97, 123)]
    frase = input()
    frase = list(frase)
    risulato = scansione(frase, alfabeto)
    if risulato >= 26:
        print('SI', end='')
    else:
        print('NO', end='')

def scansione(frase, alfabeto):
    risultato = 0
    for lettera in alfabeto:
        if lettera in frase:
            risultato += 1
    return risultato
main()