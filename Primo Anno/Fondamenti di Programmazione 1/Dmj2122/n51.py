def main():
    sequenza1 = inserimento([], input())
    sequenza2 = inserimento([], input())
    results, carattere = scan(sequenza1, sequenza2)
    print(carattere if results else 'DISGIUNTE', end='')

def inserimento(lista, x):
    while x != '.':
        lista.append(x)
        x = input()
    return lista

def scan(sequenza1, sequenza2):
    for i in range(len(sequenza1)):
        if sequenza1[i] in sequenza2:
            return True, sequenza1[i]
    return False, 0

main()