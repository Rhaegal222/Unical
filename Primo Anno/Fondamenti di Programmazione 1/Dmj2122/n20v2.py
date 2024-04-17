def main():
    print(scan(''), end='')

def scan(stringa):
    x = input()
    if x != '.':
        return scan(stringa+x)
    return ('SI' if stringa.isalpha() or stringa == '' else 'NO')
main()