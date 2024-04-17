def main():
    print(sequenza(0), end='')

def sequenza(somma):
    x = int(input())
    if x != 0:
        t = input()
        if t == 's':
            somma += x
        elif t == 'm':
            somma +=(x*60)
        elif t == 'h':
            somma +=(x*60*60)
        return sequenza(somma)
    else:
        return somma

main()