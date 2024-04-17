def main():
    S = input()
    N = int(input())
    Stringhe = LeggiStringhe(N)
    Stringhe = ordine(Stringhe)
    risultato = Check(Stringhe, S, N)
    if risultato == False:
        print(Stringhe[N-1]+Stringhe[0], end='')

def LeggiStringhe(N):
    Stringhe = []
    for i in range(N):
        Stringhe.append(input())
    return Stringhe

def ordine(Stringhe):
    for i in range(len(Stringhe)):
        for j in range(len(Stringhe)-1-i):
            if Stringhe[j] > Stringhe[j+1]:
                temp=Stringhe[j]
                Stringhe[j]=Stringhe[j+1]
                Stringhe[j+1]=temp
    return Stringhe

def Check(Stringhe, S, N):
    for i in range(len(Stringhe)):
        for j in range(len(Stringhe)):
            if i == j:
                continue
            Stringa = Stringhe[i] + Stringhe[j]
            if S == Stringa:
                print('OK', end='')
                return True
    return False
main()