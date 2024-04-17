def main():
    studenti = int(input())
    esami = int(input())
    matrice = inserimento(studenti, esami, [])
    n18, media = scan(matrice, studenti, esami, 0, 0)
    print(n18, media, end='')

def inserimento(n, m, matrice):
    for i in range(n):
        matrice.append([])
        for j in range(m):
            matrice[i].append(int(input()))
    return matrice

def scan(matrice, studenti, esami, cont, n18):
    for i in range(esami):
        if cont == studenti:
            n18 += 1
        cont = 0
        for j in range(studenti):
            if matrice[j][i] != 18:
                cont += 1
    if cont == studenti:
        n18 += 1
    
    for i in range(studenti):
        for j in range(esami-1, -1, -1):
            if matrice[i][j] < 18:
                matrice[i].pop(j)             
    
    temp = matrice[0]
    
    for i in matrice:
        if len(i) > len(temp):
            temp = i
    
    media = sum(temp) / len(temp)
    return n18, round(media)

main()