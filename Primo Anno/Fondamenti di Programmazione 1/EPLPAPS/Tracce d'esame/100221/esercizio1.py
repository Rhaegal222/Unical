def main():
    sequenza = inserimento([], input())
    print('SI' if scan(sequenza) else 'NO', end='')

def inserimento(sequenza, x):
    while x != ':':
        sequenza.append(x)
        x = input()
    return sequenza

def scan(sequenza):
    for i in range(len(sequenza)):
        if i == 0 and ((sequenza[0] != 'def') or (sequenza[2] != '(') or (sequenza[len(sequenza)-1] != ')')):
            return False
        elif i == 1 and not(scan_nome(sequenza[1])):
            return False
        elif i == 3 and sequenza[3] == ')':
            return True
        elif i > 2 and i != len(sequenza)-1 and i % 2 == 0 and sequenza[i] != ',':
            return False
        elif i > 2 and i % 2 != 0 and not(scan_nome(sequenza[i])):
            return False
    return True

def scan_nome(nome):
    for i in range(len(nome)):
        if nome[0].isdigit():
            return False
        elif not(nome[i].isalnum()) and nome[i] != '_':
            return False
    return True

main()