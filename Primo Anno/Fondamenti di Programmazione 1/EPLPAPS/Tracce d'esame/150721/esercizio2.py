def main():
    numeri = []
    print("-1 per terminare l'inserimento")
    numero = int(input())
    while numero != -1:
        numeri.append(numero)
        numero = int(input())

    print(ricorsiva(numeri, 0))

def ricorsiva(numeri, i):
    if i >= len(numeri):
        return True
    sum_div = sum(src_divisori(numeri[i]))
    if i != len(numeri)-1 and sum_div != numeri[i+1]:
        return False
    elif i == len(numeri)-1 and sum_div != numeri[0]:
        return False
    else:
        return ricorsiva(numeri, i+1)

def src_divisori(numero):
    divisori = []
    for i in range(1, numero):
        if numero % i == 0:
            divisori.append(i)
    return divisori

main()