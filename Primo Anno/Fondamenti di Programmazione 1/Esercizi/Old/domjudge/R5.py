def main():
    N = int(input())
    lista = [(input()) for i in range(N)]
    print(ricorsiva(lista, 0), end='')

def ricorsiva(lista, i):
    if i >= len(lista):
        return lista_in_stringa(lista)
    X = lista[len(lista)-i-1]
    del lista[len(lista)-i-1]
    lista.append(X)
    return ricorsiva(lista, i+1)

def lista_in_stringa(lista):
    Stringa = ''
    for i in range(len(lista)): Stringa += lista[i]
    return Stringa

main()