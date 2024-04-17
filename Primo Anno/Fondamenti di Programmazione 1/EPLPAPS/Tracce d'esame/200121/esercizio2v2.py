def main():
    estratti = inserimento([])
    giocati = inserimento([])
    scan(giocati, estratti, 0, 0)

def inserimento(numeri):
    for i in range(10):
        numeri.append(int(input()))
    return numeri

def scan(giocati, estratti, l, lmax):
    for i in giocati:
        if i in estratti:
            l += 1
        else:
            if l > lmax:
                lmax = l
            l = 0
   
    if lmax > 1 and lmax < 5:
        print(lmax, end='')
    elif lmax >= 5:
        print(5, end='')
    else:
        print(0, end='')
main()