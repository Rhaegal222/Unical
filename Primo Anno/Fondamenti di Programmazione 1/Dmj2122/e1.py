def main():
    sequenza = inserimento([], input())
    print('SI' if scan(sequenza) else 'NO', end='')

def inserimento(sequenza, x):
    while x != ':':
        sequenza.append(x)
        x = input()
    sequenza.append(x)
    return sequenza

def scan(sequenza):
    for i in range(len(sequenza)):
        if (sequenza[0] != 'def' or sequenza[len(sequenza)-2] != ')' or sequenza[2] != '('):
            return False
        elif (sequenza[1][0].isdigit() or (not('_' in sequenza[1]) and not(sequenza[1].isalnum()))):
            return False
        elif sequenza[3] == ')':
            return True
        elif (i > 2 and i % 2 != 0 and i != len(sequenza)-1):
            if (sequenza[i][0].isdigit() or (sequenza[i][0] != '_' and not(sequenza[i].isalnum()))):
                return False
        elif (i > 2 and i % 2 == 0 and i != len(sequenza)-2):
            if sequenza[i] != ',':
                return False
    return True
main()