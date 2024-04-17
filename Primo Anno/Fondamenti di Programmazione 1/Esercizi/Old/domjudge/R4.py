def main():
    X = int(input())
    N = int(input())
    lista = [int(input()) for i in range(N)]
    print(ricorsiva(lista, N, X, 0, 0), end='')

def ricorsiva(lista, N, X, C, i):
    if i >= N and C == 0:
        return 0
    
    if i >= N:
        return C + ricorsiva(lista, N, C, 0, 0)
    
    if X == lista[i]:
        lista[i] = 0
        return ricorsiva(lista, N, X, C+1, i+1)
    
    return ricorsiva(lista, N, X, C, i+1)
main()