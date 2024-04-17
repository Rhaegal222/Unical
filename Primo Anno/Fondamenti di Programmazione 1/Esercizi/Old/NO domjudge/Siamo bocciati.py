def main():
    numeri_giocati = numeri()
    numeri_estratti = numeri()
    conteggio = confronto(numeri_giocati, numeri_estratti)
    print(conteggio)

def numeri():
    lista = []
    for i in range(4):
        lista.append(int(input()))
    return lista

def confronto(numeri_giocati, numeri_estratti):
    cont = 1
    lista2 = []
    for i in range(len(numeri_giocati)):
        for j in range(len(numeri_estratti)):
            if numeri_giocati[i] == numeri_estratti[j]:
                   lista2.append(j)
    lista2.sort()
    for i in range(len(lista2)-1):
        if lista2[i]+1 == lista2[i+1]:
            cont += 1
    if cont == 1:
        cont += 1
    if cont >= 5:
        cont = 5
    return cont

main()
