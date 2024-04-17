def main():
    print(sequenza([]), end='')

def sequenza(lista):
    x = int(input())
    if x != 0:
        t = input()
        if t == 's':
            lista.append(x)
        elif t == 'm':
            lista.append(x*60)
        elif t == 'h':
            lista.append(x*60*60)
        return sequenza(lista)
    else:
        return sum(lista)

main()