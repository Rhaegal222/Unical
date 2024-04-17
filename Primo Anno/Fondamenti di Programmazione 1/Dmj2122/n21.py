def main():
    print('SI' if inserimento(input(), True) else 'NO', end='')

def inserimento(x, cond):
    while x != '.':
        x = input()
        if x.isalpha():
            cond = False
    return cond

main()