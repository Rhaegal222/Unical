def stampa(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j],end="")
        print()

def stampaParolaNascosta(matrice):
    parolaNascosta = ''
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j]!=0:
                parolaNascosta+=matrice[i][j]
    return parolaNascosta

def rimuovi_parola(matrice, parola, riga, colonna, cond):
    if cond:
        for i in range(colonna, colonna-1-len(parola), -1):
            matrice[i][riga] = 0
        return matrice   
    else:
        for i in range(colonna, colonna-len(parola), -1):
            matrice[riga][i] = 0
        return matrice
        
def scansionaMatrice(parole, matrice, indice):
    if indice >= len(parole):
        return matrice
    
    parola = list(parole[indice])
    point = 0
    
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if point < len(parola)-1 and (parola[point] != matrice[i][j] or matrice[i][j+1] != parola[point+1]):
                if j > len(matrice[i])-len(parola):
                    point = 0
                    break
                else:
                    point = 0
            elif point >= len(parola)-1:
                matrice = rimuovi_parola(matrice, parola, i, j, False)
                return scansionaMatrice(parole, matrice, indice+1)
            else:
                point += 1

    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if point < len(parola)-1 and (parola[point] != matrice[j][i] or matrice[j+1][i] != parola[point+1]):
                if j > len(matrice[i])-len(parola):
                    point = 0
                    break
                else:
                    point = 0
            elif point >= len(parola)-1:
                matrice = rimuovi_parola(matrice, parola, i, j, True)
                return scansionaMatrice(parole, matrice, indice+1)
            else:
                point += 1

def generaMatrice(N,M,matrice):
    for i in range(N):
        matrice.append([])
        for j in range(M):
            matrice[i].append(input("Caricare lettera per lettera le parole da inserire nella matrice: "))
    return matrice     

def main():
    #righe = int(input("Inserire il numero di righe (N): "))
    #colonne = int(input("Inserire il numero delle colonne (M): "))
    #matrice = generaMatrice(righe, colonne, [])
    matrice =[list('CENA'), list('OREU'), list('RSNS'), list('OIAA')]
    stampa(matrice)
    #n_parole = int(input("Inserire il numero di parole da rimuovere: "))
    #parole = [input() for i in range(n_parole)]
    parole = ['CENA', 'ORO', 'RE']
    matrice = scansionaMatrice(parole, matrice, 0)
    print(stampaParolaNascosta(matrice), end='')
main()
