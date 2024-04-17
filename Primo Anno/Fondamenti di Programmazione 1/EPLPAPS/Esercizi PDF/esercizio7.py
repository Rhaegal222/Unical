def main():
    n = int(input())
    frase = list(input())

    for i in frase:
        if i == ' ':
            frase.remove(i)

    f1 = []
    for i in range(n-1):
        f1.append(frase[i])
    f2 = []
    for i in range(n-1, len(frase)):
        f2.append(frase[i])
    
    f1.sort()
    f2.sort()
    
    if f1 == f2:
        print('SI', end = '')
    else:
        print('NO', end='')

main()