def main():
    lista = insert([])
    print(scan(lista), end='')

def insert(lista):
    x = int(input())
    if x != -1:
        lista.append(x)
        return insert(lista)
    else:
        return lista

def scan(lista):
    if len(lista) <= 0: return 'VUOTO'
    for i in lista:
        if i < 0 or i > 9:
            return 'ERRORE'
    stringa = ''
    for i in lista: stringa += str(i)
    numero = int(stringa)
    return str(numero)+'\nSI' if numero % 3 == 0 else str(numero)+'\nNO'
main()