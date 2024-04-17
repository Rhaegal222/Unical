from random import randint
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
    parola = list(parola)
    lunghezzaparola = list(range( 0,len(parola)))
    parolascombinata=[]
    c = 0

    for i in range (0,len(lunghezzaparola)):
        c=randint(0,len(lunghezzaparola)-1)
        val=lunghezzaparola[c]
        parolascombinata.append(parola[val])
        lunghezzaparola.remove(val)
    
    stringa=''
    for i in parolascombinata:
        stringa+=i
    print(parola)

    return new if new != stringa else gen(stringa, '')

main()