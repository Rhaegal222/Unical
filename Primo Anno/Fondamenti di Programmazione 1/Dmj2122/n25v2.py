def main():
    for i in scan(0, [], None): print(i)

def scan(somma, lista, temp):
    x = int(input())
    if x == 0 and temp == 0:
        return lista
    if x != 0:
        somma += x
    else:
        lista.append(somma)
        somma = 0
    return scan(somma, lista, x)

main()