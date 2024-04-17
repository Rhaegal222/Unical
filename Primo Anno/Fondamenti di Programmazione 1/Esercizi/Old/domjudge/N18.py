N = str
c = 0
s = 0

lista = []

while c <= 1 and s < 1:
    N = (input())
    lista.append(N)
    if N == 'o':
        c = c + 1
    elif N == 'k' and c == 1:
        s = s + 1
    else:
        c = 0
        s = 0

print(len(lista) - 2, end="")