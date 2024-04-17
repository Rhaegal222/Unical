from random import randint
def main():
    n = int(input()) 
    R_min = int(input()) 
    R_max = int(input()) 
    C_min = int(input()) 
    C_max = int(input()) 
    Tot_min = int(input()) 
    Tot_max = int(input())
    T = int(input())
    
    cont = 0
    sol = False
    
    while not(sol) and cont < T:
        matrice = [[randint(0, 1) for j in range(n)] for i in range(n)]
        sol = generator(matrice, R_min, R_max, C_min, C_max, Tot_min, Tot_max)
        cont += 1
    
    if sol: stampa(matrice)

def stampa(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 0:
                print('| |', end='')
            else:
                print('|*|', end='')
        print()
    
def generator(matrice, R_min, R_max, C_min, C_max, Tot_min, Tot_max):
    sum = 0
    for i in matrice:
        sum += i.count(0)
        if i.count(0) < R_min or i.count(0) > R_max:
            return False
    
    inverted = inverter(matrice)
    
    for i in inverted:
        if i.count(1) < C_min or i.count(1) > C_max:
            return False
    
    if sum < Tot_min or sum > Tot_max:
        return False
    return matrice

def inverter(matrice):
    empty = []
    for i in range(len(matrice)):
        empty.append([])
        for j in range(len(matrice)):
            empty[i].append(matrice[j][i])
    return empty

main()