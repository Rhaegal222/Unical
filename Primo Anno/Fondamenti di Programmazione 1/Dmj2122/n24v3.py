def main():
    vocali = ['a', 'e', 'i', 'o', 'u']
    sequenza = inserimento(input(), [])
    print(scan(sequenza, vocali, 1), end='')

def inserimento(x, sequenza):
    while x != '.':
        sequenza.append(x)
        x = input()
    return sequenza

def scan(sequenza, vocali, cont):
    for i in range(len(sequenza)-1):
        if (sequenza[i] in vocali) and (sequenza[i+1] in vocali):
            cont += 1
        if not(sequenza[i] in vocali) and not(sequenza[i+1] in vocali):
            cont += 1 
    return(cont if len(sequenza) > 0 else 0)





        



main()