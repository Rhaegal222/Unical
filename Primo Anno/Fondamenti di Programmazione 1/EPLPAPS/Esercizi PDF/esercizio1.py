import random
def main():
    parola1 = input()
    parola2 = input()
    print('SI' if uguali(parola1, parola2) else gen(parola1, ''))

def uguali(parola1, parola2):
    parola1 = sorting(list(parola1))
    parola2 = sorting(list(parola2))
    return(True if parola1 == parola2 else False)

def sorting(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def gen(parola, new):
    stringa = ''
    for i in parola: stringa += i
    parola = list(parola)
    random.shuffle(parola)
    for i in parola: new += i
    return new if new != stringa else gen(stringa, '')

main()