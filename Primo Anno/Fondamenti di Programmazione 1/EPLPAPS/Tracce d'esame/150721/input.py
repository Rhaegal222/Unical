def main():
    N = 6
    D = [["ppp1", "pippo",  "20"], ["plt5", "pluto", "22"], ["tpln3", "topolino", "21"], ["mnn2", 
    "minnie", "26"], ["clrbll", "clarabella","31"], ["rzo1", "orazio","28"]]  
    E = [["ppp1", "NO"], ["tpln3", "SI"], ["mnn2", "NO"], ["plt5", "SI"], ["rzo1","SI"], ["clrbll", "SI"]]  
    M = 2 
    P = [["tpln5", "topolina", "28"], ["plt5", "pluto", "22"]]

    print(N)
    printm(D)
    printm(E)
    print(M)
    printm(P)

def printm(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j])
main()