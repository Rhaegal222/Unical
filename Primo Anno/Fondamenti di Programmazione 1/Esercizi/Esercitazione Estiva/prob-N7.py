def main():
    condizione = False
    risultato = inserimento(condizione, 0)
    stampa(risultato)
    
def inserimento(condizione, x):
    x = int(input())
    if x == 5:
        return condizione
    if x % 5 == 0:
        condizione = True
    return inserimento(condizione, x)

def stampa(risultato):
    if risultato:
        print('ALMENO 1', end='')
    else:
        print('NESSUNO', end='')
    
main()
