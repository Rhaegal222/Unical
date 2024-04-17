def main():
    N = input()
    M = int(input())
    print(rotazione(N, M, 0))

def rotazione(N, M, i):
    if i == len(N):
        return False
    if int(N)%M == 0:
        return True
    else:
        N=N[1:]+N[0]
        return rotazione(N,M,i+1)
main()
