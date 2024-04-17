A = []
B = []
Stringa = ''

for i in range(26):
    x = input()
    A.append(x)

N = int(input())

for i in range(N):
    x = input()
    B.append(x)

for i in range(N):
    for j in range(26):
        if int(B[i])==j:
            Stringa = Stringa + A[j]
            break
            
print(Stringa, sep='', end='')
