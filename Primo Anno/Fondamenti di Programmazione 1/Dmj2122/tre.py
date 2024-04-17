x = int(input())
matrice = []
cont = 1

for i in range(10):
    matrice.append([])
    for j in range(10):
        matrice[i].append(cont)
        cont += 1
        if cont > x:
            cont = 1
somma = 0
for i in range(10):
    for j in range(10):
        if i + j == 9:
            somma += matrice[i][j]

print(somma, end='')
