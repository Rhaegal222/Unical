def main():
    print('SI' if inserimento(int(input()), True, False, 0) else 'NO', end='')

def inserimento(x, crescente, decrescente, cont):
    while x != 0:
        temp = x
        x = int(input())
        if x != 0:
            cont += 1
            if decrescente and not(crescente):
                if x >= temp:
                    crescente = True
            elif crescente and not(decrescente):
                if x <= temp:
                    decrescente = True
                    crescente = False
        if cont < 2:
            crescente = True
    return (True if not(crescente) and decrescente else False)
            
main()