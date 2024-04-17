def main():
    lista = [(int(input())) for i in range(int(input()))]
    print('SI' if ricorsiva(lista, 0) else 'NO', end='')

def ricorsiva(lista, indice):
    if indice >= (len(lista)//2):
        return True
    elif lista[indice] != lista[(len(lista)//2)+indice]:
        return False
    return ricorsiva(lista, indice+1)

main()