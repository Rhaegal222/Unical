def main():
    lista = inserimento([], int(input()))
    seq = collatz(lista[0], [])
    print(True if seq == lista else False)

def inserimento(lista, x):
    while x != 1:
        lista.append(x)
        x = int(input())
    lista.append(x)
    return lista

def collatz(numero, lista):
    if numero == 1:
        lista.append(int(numero))
        return lista
    if numero % 2 == 0:
        lista.append(int(numero))
        return collatz(numero/2, lista)
    else:
        lista.append(int(numero))
        return collatz((numero*3)+1, lista)

main()