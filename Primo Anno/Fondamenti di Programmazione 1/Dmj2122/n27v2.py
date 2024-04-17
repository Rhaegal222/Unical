def main():
    n = int(input())
    sequenza = insert([])
    print(scan(sequenza, n, 0), end='')

def insert(sequenza):
    x = int(input())
    while x != -1:
        sequenza.append(x)
        x = int(input())
    return sequenza

def scan(sequenza, n, cont):
    for i in sequenza:
        if i <= n:
            cont += 1
        else:
            if cont < n: cont = 0
    return 'OK' if cont >= n else  'NO'

main()