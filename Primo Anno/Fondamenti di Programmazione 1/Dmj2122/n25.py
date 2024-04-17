def main():
    lista = inserimento([], 0)
    scan(lista, 0)
def inserimento(lista, cont0):
    if cont0 >= 2:
        return lista
    else:
        n = int(input())
        lista.append(n)
        return(inserimento(lista, cont0+1) if n == 0 else inserimento(lista, 0))

def scan(lista, Somma):
    for i in range(len(lista)-1):
        if lista[i] != 0:
            Somma += lista[i]
        else:
            print(Somma)
            Somma = 0
main()
