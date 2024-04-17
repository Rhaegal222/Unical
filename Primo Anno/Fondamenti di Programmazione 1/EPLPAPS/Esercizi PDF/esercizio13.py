def main():
    n = int(input()) #dimensione liste
    car = [input() for i in range(n)] #lista paarola
    pos = [int(input()) for i in range(n-1)] #lista numeri
    righe = int(input())
    colonne = int(input())
    mat = [[input()for j in range(colonne)] for i in range(righe)]
    #car = list('casale')
    #pos = [6,2,3,2,1]
    #mat = ['m n c i l m'.split(' '), 'i o a p s a'.split(' '), 'p a a l e c'.split(' '), 'v b w s x u'.split(' ')]
    ricorsiva = checkr(mat, car, pos, 1, 0, '', False, 0, 0)
    non_ricorsiva = check(mat, car, pos, 1, 0)
    print('ERRORE' if not(ricorsiva) else ricorsiva)
    print('ERRORE' if not(non_ricorsiva) else non_ricorsiva, end='')

#ricorsiva:
def checkr(mat, car, pos, indice, cont, string, inizio, i, j):
    if indice > len(pos)-1:
        return string
    if i < len(mat):
        if j < len(mat[0]):
            if inizio and indice < len(pos):
                if cont == pos[indice-1]-1 and mat[i][j] != car[indice]:
                    return False
                elif cont < pos[indice-1]-1:
                    cont += 1
                    string += mat[i][j]
                    return checkr(mat, car, pos, indice, cont, string, inizio, i, j+1)
                else:
                    cont = 0
                    indice += 1
                    return checkr(mat, car, pos, indice, cont, string, inizio, i, j+1)
            if mat[i][j] == car[indice-1] and not(inizio):
                inizio = True
                return checkr(mat, car, pos, indice, cont, string, inizio, i, j+1)
            else:
                return checkr(mat, car, pos, indice, cont, string, inizio, i, j+1)
        else:
            return checkr(mat, car, pos, indice, cont, string, inizio, i+1, 0)
    else:
        return string

#non ricorsiva: 
def check(mat, car, pos, indice, cont):
    string = ''
    inizio = False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if inizio and indice < len(pos):
                if cont == pos[indice-1]-1 and mat[i][j] != car[indice]:
                    return False
                elif cont < pos[indice-1]-1:
                    cont += 1
                    string += mat[i][j]
                else:
                    cont = 0
                    indice += 1
            if mat[i][j] == car[indice-1] and not(inizio):
                inizio = True
    return string

main()