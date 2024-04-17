def main():
    lista = [4, 3, 3, 6, 2, 3, 3]
    print(scan(lista, 0))

def scan(lista, cont):
    if (lista[0] + lista[1]) % 2 == 0:
        for i in range(1, len(lista)):
            cont += 1
            if (lista[i] + lista[i-1]) % 2 == 0 and cont % 2 == 0:
                return False
    elif (lista[0] + lista[1]) % 2 != 0:
        for i in range(1, len(lista)):
            cont += 1
            if (lista[i] + lista[i-1]) % 2 != 0 and cont % 2 == 0:
                return False
    return True

main()
