def main():
    k = int(input())
    matrice = riempimento(k, [int(input()) for i in range(k)], int(input()), int(input()))
    stampa(matrice)

def riempimento(nint, lint, row, column):
    matrice = [[0 for j in range(column)] for i in range(row)]
    
    x = 0
    y = 1
    lim = 0
    while lim <= (row*column):
        
        #Compone la prima riga:
        for i in range(x, column-x):
            matrice[x][i] = lint[lim%len(lint)]
            lim += 1

        if lim >= (row*column):
            return matrice

        #Compone l'ultima colonna:
        for i in range(y, row-x):
            matrice[i][column-y] = lint[lim%len(lint)]
            lim += 1

        if lim >= (row*column):
            return matrice

        #compone l'ultima riga:
        for i in range(column-x-2, x-1, -1):
            matrice[row-x-1][i] = lint[lim%len(lint)]
            lim += 1
        
        if lim >= (row*column):
            return matrice

        #compone la prima colonna:
        for i in range(row-x-2, y-1, -1):
            matrice[i][x] = lint[lim%len(lint)]
            lim += 1

        if lim >= (row*column):
            return matrice
        
        x+=1
        y+=1
    
def stampa(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            print(matrice[i][j], end='')
        print()

main()
