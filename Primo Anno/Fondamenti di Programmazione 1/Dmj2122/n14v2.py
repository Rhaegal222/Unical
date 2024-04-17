def main():
    insert('', int(input()))

def insert(stringa, x):
    while x != -1:
        if x >= 0 and x<=9 and stringa != 'ERRORE':
            stringa += str(x)
        else:
            stringa = 'ERRORE'
        x = int(input())
    print(stringa if stringa != '' else 'VUOTO', end = '')
    if stringa != 'ERRORE' and stringa != '':
        print('\nSI' if int(stringa) % 3 == 0 else 'NO', end = '')

main()