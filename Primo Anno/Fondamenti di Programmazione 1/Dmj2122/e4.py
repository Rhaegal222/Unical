def main():
    studenti = int(input())
    esami = int(input())
    matrice = [[int(input()) for j in range(esami)] for i in range(studenti)]
    inv = [[matrice[j][i] for j in range(studenti)] for i in range(esami)]

    count = 0
    best = matrice[0]
    
    for i in inv:
        if i.count(18) == 0:
            count += 1
    
    for i in matrice:
        if i.count(0) < best.count(0):
            best = i
    
    print(count, round(sum(best)/(len(best)-best.count(0))), end='')

main()


