def main():
    N = input()
    conta_cifre(N)

def conta_cifre(N):
    New_N = ''
    cont = 1
    for i in range(len(N)-1):
        if N[i] == N[i+1]:
            cont += 1
        else:
            New_N = New_N + str(cont) + N[i]
            cont = 1
    New_N += str(cont) + N [- 1]
    print(New_N, len(New_N), end='')
main()