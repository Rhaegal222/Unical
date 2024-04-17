def non_ricorsiva(numero, matrice):
    Somma = 0
    for i in range(numero):
        for j in range(numero):
            if i + j == numero - 1:
                Somma += int(matrice[i][j])
    return Somma

def ricorsiva(numero, matrice, i):
    if i >= numero:
        return 0
    return matrice[i][numero-1-i] + ricorsiva(numero, matrice, i+1)

N = int(input())
M = []

for i in range(N):
    M.append([])
    for j in range(N):
        x = int(input())
        M[i].append(x)

print(non_ricorsiva(N, M),';', ricorsiva(N, M, 0), end='', sep='')

    
