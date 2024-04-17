def main():
    x, y = inserimento()
    numeri_dispari(x, y)

def inserimento():
    x = int(input())
    y = int(input())
    return x, y

def numeri_dispari(x, y):
    somma = 0
    for i in range(x, y+1):
        if i % 2 != 0:
            somma += i
    print(somma, end='')
        

main()
