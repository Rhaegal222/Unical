def main():
    Stringa = input()
    Stringa2 = codifica(Stringa)
    split(Stringa2)

def codifica(Stringa):
    vocali = ['a', 'e', 'i', 'o', 'u']
    Stringa2 = ''
    cont = 0
    for i in Stringa:
        cont = 0
        for j in range(len(vocali)):
            if i == vocali[j]:
                i = vocali[j]+'f'+vocali[j]
                Stringa2 += i
                cont += 1
            else:
                if j == len(vocali)-1 and cont == 0:
                    Stringa2 += i
    return Stringa2
# Divide la stringa a metà e inverte le metà
def split(Stringa2):
    Stringa = ''
    for i in range(len(Stringa2)//2, len(Stringa2)):
        Stringa += Stringa2[i]
    for i in range(len(Stringa2)//2):
        Stringa += Stringa2[i]
    print(Stringa, end='')

main()