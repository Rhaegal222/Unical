def main():
    M = int(input())
    N = int(input())
    matrice = crea_matrice(M, N)
    miglior_giudice = scan_giudice(matrice, M, N)
    peggior_cantante = scan_cantante(matrice, M, N)
    print(miglior_giudice, peggior_cantante, end='')

def crea_matrice(M, N):
    matrice = []
    for i in range(M):
        matrice.append([])
        for j in range(N):
            matrice[i].append(int(input()))
    return matrice

def scan_giudice(matrice, M, N):
    lista_giudici = []
    for i in range(M):
        cont = 0
        for j in range(N):
            if matrice[i][j] > 5:
                cont += 1
        lista_giudici.append(sum([cont, i]))
    migliore = lista_giudici.index(max(lista_giudici))
    return migliore

def scan_cantante(matrice, M, N):
    voti_cantanti = []
    lista_cantanti = []
    for i in range(N):
        cont = 0
        for j in range(M):
            cont += matrice[j][i]
        voti_cantanti.append(cont)
        lista_cantanti.append(i)
    for i in range(len(lista_cantanti)):
        if min(voti_cantanti) == voti_cantanti[i] and i == lista_cantanti[i]:
            peggiore = lista_cantanti[i]
    return peggiore

main()