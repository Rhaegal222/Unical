def main():
    print(scan(''), end='')

def scan(stringa):
    x = input()
    return(scan(stringa+x) if x != '.' else 'SI' if stringa.isalpha() or stringa == '' else 'NO')
main()