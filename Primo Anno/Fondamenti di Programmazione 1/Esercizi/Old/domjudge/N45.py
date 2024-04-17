def main():
    N = (input())
    if N!=0:
        sequenza = list(N)
        S = bubbleSort(sequenza)
        Min = LiS(S)
        iS = bubbleSortInverted(sequenza)
        Max = LiS(iS)
        print(int(Max)-int(Min), end='')
    else:
        print('0', end='')

def bubbleSort(S):
    for i in range(len(S)):
        for j in range(len(S)-1):
            if S[j] > S[j+1]:
                temp=S[j]
                S[j]=S[j+1]
                S[j+1]=temp
    return S

def bubbleSortInverted(iS):
    for x in range(len(iS)):
        for y in range(len(iS)-1):
            if iS[y] < iS[y+1]:
                temp=iS[y]
                iS[y]=iS[y+1]
                iS[y+1]=temp
    return iS

def LiS(L):
    String = ''
    for i in range(len(L)):
        String = String + str(L[i])
    return String
main()
