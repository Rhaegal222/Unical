def main():
    lista = [input() for i in range(100)]
    vocali = ['a', 'e', 'i', 'o', 'u']
    print('OK' if scan(vocali, lista, 0) < 2 else 'ERRORE', end='')

def scan(vocali, lista, count):
    for i in vocali:
        if i in lista: 
            count += 1
    return count
main()