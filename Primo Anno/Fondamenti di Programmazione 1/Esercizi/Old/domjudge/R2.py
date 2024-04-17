def main():
    N = int(input())
    lista = []
    lista_creata = crea_lista(N, lista, 0)
    print(scansiona_lista(N, lista_creata, 0, N//2), end='')

def crea_lista(N, lista, i):
    if i < N:
        lista.append(int(input()))
        return crea_lista(N, lista, i+1)
    else:
        return lista

def scansiona_lista(N, lista, i, j):
    if j == N:
        return 'SI'
    if lista[i] == lista[j]:
        return scansiona_lista(N, lista, i+1, j+1)
    else:
        return 'NO'
main()