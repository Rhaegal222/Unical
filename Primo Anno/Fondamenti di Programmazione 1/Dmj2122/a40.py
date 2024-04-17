def main():
    print(stampa(1000), end='')

def stampa(x):
    lista = ilista(x, [])
    if len(lista) <= 0:
        return 'VUOTA'
    else:
        media = cmedia(lista)
        for i in lista:
            if i >= media and i <= x:
                x = i
        return x

def ilista(x, lista):
    while x != -50:
        x = int(input())
        if x != -50 and x < 1000:
            lista.append(x)
    return lista
    
def cmedia(lista): 
    media = sum(lista) // len(lista)
    return media

main()