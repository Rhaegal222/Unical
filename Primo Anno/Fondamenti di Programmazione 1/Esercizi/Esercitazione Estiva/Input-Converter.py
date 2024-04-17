def main():
    inserito = input()
    conversione(inserito)

def conversione(inserito):
    stringa = ''
    for i in inserito:
        if i == ' ':
            i = '\n'
            stringa += i
        else:
            stringa += i
    print()
    print(stringa)
    print()

main()