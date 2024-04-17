L = [3, 5, 2, 70, 2, 5 ,3]
N = len(L)
palindromo = True
for i in range (N):
    if L[i] != L[N-1-i]:
        palindromo = False
if palindromo:
    print('SI')
else:
    print('NO')