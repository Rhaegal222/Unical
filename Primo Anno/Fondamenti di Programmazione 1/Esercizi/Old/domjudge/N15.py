N1 = int(input())
N2 = int(input())
N3 = int(input())
cont = 0
while N1 != 9 or N2 != 9 or N3 != 9:
    if N1 == N2 and N2 == N3 and N1 == N3:
        cont += 1
    N1 = N2
    N2 = N3
    N3 = int(input())

print(cont,end="")