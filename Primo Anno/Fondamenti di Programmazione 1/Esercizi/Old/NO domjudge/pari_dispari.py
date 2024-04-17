def main():
    k = int(input())
    lista = crea_lista(k, [], 0)
    print(scansiona_lista(lista, 0, False))

def crea_lista(k, lista, i):
    if i >= k:
        return lista
    else:
        lista.append(int(input()))
        return crea_lista(k, lista, i+1)

def scansiona_lista(lista, i, status):
    if i == len(lista)-1:
        return status
    if (lista[0] + lista[1])%2 != 0:
        status = scansiona_lista_dispari(lista, 0, False)
        return status
    if i % 2 == 0:
        if (lista[i] + lista[i+1])%2 == 0:
            return scansiona_lista(lista, i+1, True)
        else:
            status = False
            return status
    else:                
        if (lista[i] + lista[i+1])%2 != 0:
            return scansiona_lista(lista, i+1, True)
        else:
            status = False
            return status

def scansiona_lista_dispari(lista, i, status):
    if i == len(lista)-1:
        return status
    if i % 2 == 0:
        if (lista[i] + lista[i+1])%2 != 0:
            return scansiona_lista_dispari(lista, i+1, True)
        else:
            status = False
            return status
    else:                
        if (lista[i] + lista[i+1])%2 == 0:
            return scansiona_lista_dispari(lista, i+1, True)
        else:
            status = False
            return status
    
main()
