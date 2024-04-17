I = [1, 13]
C = ['a', '*', 'w']

for i in range(len(I)):
    for j in range(len(C)):
        for k in range(len(C)):
            if i != j:
                print(str(I[i])+C[j]+C[k])

print('Ricorsiva: ')
print()

def ricorsione(I, C, i, j, k):
    if i == len(I):
        return
    if j < len(C):
        if k < len(C):
            if j != k:
                print(str(I[i])+C[j]+C[k])
            return ricorsione(I, C, i, j, k+1)
        else:
            return ricorsione(I, C, i, j+1, 0)
    else:
        return ricorsione(I, C, i+1, 0, 0)

ricorsione(I, C, 0, 0, 0)