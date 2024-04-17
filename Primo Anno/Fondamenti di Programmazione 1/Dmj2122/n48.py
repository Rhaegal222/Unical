def main():
    lista = inserimento([], int(input()))
    if len(lista) < 1:
        print('Empty', end='')
    else:
        sequenze = scan(lista, 0, [[]])
        print('\n', result(sequenze, sequenze[0]), sep = '', end='')

def inserimento(lista, x):
    while x >= 0:
        lista.append(x)
        x = int(input())
    return lista

def scan(lista, cont, sequenze):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            sequenze[cont].append(lista[i])
            sequenze.append([])
            cont += 1
        else:
            sequenze[cont].append(lista[i])
    if i < len(lista): sequenze[cont].append(lista[i+1])
    return sequenze

def result(sequenze, temp):
    for i in sequenze:
        if len(i) > len(temp):
            temp = i
    for i in temp:
        print(i, end='')
    return len(temp)

main()