def main():
    lati = inserimento()
    esito = calcolo(lati, 2, True)
    if esito:
        tipo_triangolo(lati)
    else:
        print('NO', end='')

def inserimento():
    lista = []
    for i in range(3):
        lista.append(int(input()))
    return lista

def calcolo(lati, i, esito):
    if i == 0:
        return esito
    elif lati[i]+lati[i-1] > lati[i-i]:
        return calcolo(lati, i-1, esito)
    else:
        esito = False
        return calcolo(lati, i-1, esito)

def tipo_triangolo(lati):
    if lati[0] == lati[1] and lati[0] == lati[2]:
        print('TRIANGOLO EQUILATERO', end = '')
    elif lati[0] != lati[1] and lati[0] != lati[2] and lati[1] != lati[2]:
        print('TRIANGOLO SCALENO', end = '')
    else:
        print('TRIANGOLO ISOSCELE', end = '')
main()
