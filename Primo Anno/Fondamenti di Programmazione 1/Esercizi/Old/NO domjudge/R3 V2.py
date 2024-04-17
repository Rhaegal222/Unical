def main():
    numero = int(input())
    matrice = crea_matrice(numero)
    print(non_ricorsiva(numero, matrice),';', ricorsiva(numero, matrice, 0), sep='', end='')

def crea_matrice(numero):
    matrice = []
    for i in range(numero):
        matrice.append([])
        for j in range(numero):
            matrice[i].append(int(input()))
    return matrice

def non_ricorsiva(numero, matrice):
    Somma = 0
    for i in range(numero):
        Somma += matrice[i][numero-1-i]
    return Somma

def ricorsiva(numero, matrice, i):
    if i >= numero:
        return 0
    return matrice[i][numero-1-i] + ricorsiva(numero, matrice, i+1)
main()