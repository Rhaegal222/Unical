def main():
    numeri = [int(input()) for i in range(7)]
    pari, dispari = pari_dispari(numeri)
    print(ricorsiva(numeri, 0, pari, dispari), end='')

def ricorsiva(numeri, i, pari, dispari):
    if i >= len(numeri)-1:
        return True
    somma = numeri[i] + numeri[i+1]
    if somma % 2 == 0 and dispari:
        return False
    elif somma % 2 != 0 and pari:
        return False
    return ricorsiva(numeri, i+1, not(pari), not(dispari))

def pari_dispari(numeri):
    if (numeri[0]+numeri[1])%2==0:
        return True, False
    else:
        return False, True
main()