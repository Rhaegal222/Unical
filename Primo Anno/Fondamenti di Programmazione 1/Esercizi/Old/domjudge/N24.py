N = input()
M = None
vocali = ['a', 'e', 'i', 'o', 'u', None]
cont = 0
while N != '.':
    if N != '.':
        if (N in vocali and M in vocali) or (N not in vocali and M not in vocali):
            cont += 1
    M = N
    N = input()
print(cont, end="")