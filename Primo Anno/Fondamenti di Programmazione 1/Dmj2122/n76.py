def main():
    giudici = int(input())
    cantanti = int(input())
    matrice = [[int(input()) for j in range(cantanti)] for i in range(giudici)]
    giudice, cantante = scan(matrice)
    print(giudice, cantante, end='')

def scan(matrice):
    cantante = matrice_inv(matrice)
    giudice = voti_5(matrice)
    return giudice, cantante

def voti_5(matrice):
    voti_giudici = []   
    for i in range(len(matrice)):
        voti_giudici.append([])
        for j in range(len(matrice[i])):
            if matrice[i][j] > 5:
                voti_giudici[i].append(matrice[i][j])

    giudice_buono = 0
    for i in range(1, len(voti_giudici)):
        if len(voti_giudici[i]) >= len(voti_giudici[giudice_buono]):
            giudice_buono = i
    return giudice_buono

def matrice_inv(matrice):
    matrice_inv = [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]
    cantante = 0
    for i in range(1, len(matrice_inv)):
        if sum(matrice_inv[i]) <= sum(matrice_inv[cantante]):
            cantante = i
    return cantante
main()