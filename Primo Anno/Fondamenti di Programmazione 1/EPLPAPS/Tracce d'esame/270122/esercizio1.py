def cerca_divisori(numero):
    divisori = []
    
    for i in range(2, numero+1):
        if numero % i == 0:
            divisori.append(i)

    for i in range(len(divisori)):
        for j in range(2, i):
            if divisori[i] % j == 0:
                divisori[i] = '.'
                break

    nuova = []
    
    for i in range(len(divisori)):
        if divisori[i] != '.':
            nuova.append(divisori[i])

    return nuova

def fusione(A, B):
    lista = B.copy()
    for i in A:
        if i not in B:
            lista.append(i)
    return lista

def main():
    A = int(input())
    B = int(input())
    C = int(input())

    divisori_A = cerca_divisori(A)
    divisori_B = cerca_divisori(B)
    divisori = fusione(divisori_A, divisori_B)

    if len(divisori) >= C:
        print('SI', end='')
    else:
        print('NO', end='')

main()