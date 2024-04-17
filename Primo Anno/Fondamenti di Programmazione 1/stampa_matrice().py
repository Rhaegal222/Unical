def stampa_matrice(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j], ' ', end='')
        print()
stampa_matrice()