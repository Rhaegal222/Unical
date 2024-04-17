def main():
    print('ALMENO UNA' if inserimento(input(), False) else 'NESSUNA', end='')

def inserimento(x, cond):
    while x != '*':
        if x.isdigit():
            cond = True
        x = input()
    return cond

main()