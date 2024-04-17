def main():
    numeri = inserisci_numeri(0, [])
    if len(numeri) == 0:
            print ('VUOTA', end='')
    else:
        media = calcola_media(numeri, 0, 0)
        scan_lista = scanner(numeri, media, 0)

def inserisci_numeri(numero, lista):
    numero = int(input())
    if numero != -50:        
        lista.append(numero)
        return inserisci_numeri(numero, lista)
    else:
        return lista        

def calcola_media(numeri, i, media):
    if i >= len(numeri):
        media = media//len(numeri)
        return media
    else:
        media = media + numeri[i]
        return calcola_media(numeri, i+1, media)

def scanner(numeri, media, i):
    if i >= len(numeri):
        numeri.sort()
        print(numeri[0], end='')
    else:
        if numeri[i] < media:
            numeri.pop(i)
            return scanner(numeri, media, i)
        return scanner(numeri, media, i+1)
main()