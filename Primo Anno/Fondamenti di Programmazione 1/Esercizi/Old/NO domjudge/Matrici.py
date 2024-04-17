x = input()
x = x.replace(' ', '')
N = int(input())
M = []
c = 0
L = list(x)

for i in range(N):
    M.append([])
    for j in range(N):
        M[i].append(L[c])
        c += 1
    

for i in range(N):
    for j in range(N):
        print(M[i][j], end='')
    print()

print()
print('Diagonale principale')
for i in range(N):
    for j in range(N):
        if i == j:
            print(M[i][j], end='')
        else:
            print(' ', end='')
    print()

print()
print('Diagonale secondaria')
for i in range(N):
    for j in range(N):
        if i + j == N - 1:
            print(M[i][j], end='')
        else:
            print(' ', end='')
    print()

print()
print('Diagonale secondaria alternativa')
for i in range(N):
    for j in range(N-i-1, -1, -1):
            print(M[i][j], end='')
            break
    print()

print('Diagonale secondaria alternativa 2')
for i in range(N):
    print(M[i][N-1-i])
          
print()
print('Croce')
if N % 2 != 0:
    for i in range(N):
        for j in range(N):
            if i == N // 2 or j == N // 2:
                print(M[i][j], end='')
            else:
                print(' ', end='')
        print()
else:
    print('Niente croce')


        
