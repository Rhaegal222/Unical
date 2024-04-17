import random
random.seed(0)
P1 = 0
NCP = 0
cont1 = 0
cont2 = 0
while cont1 < 3 and cont2 < 3:
    P1 = input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):")

    if P1 != '3' and P1 != '2' and P1 != '1':
        continue

    NCP = str(random.randint(1, 3))

    if P1 == '1':
        print("hai giocato sasso")
    elif P1 == '2':
        print("hai giocato carta")
    elif P1 == '3':
        print("hai giocato forbice")

    if NCP == '1':
        print("il PC ha giocato sasso")
    elif NCP == '2':
        print("il PC ha giocato carta")
    elif NCP == '3':
        print("il PC ha giocato forbice")

    if P1 == NCP:
        print("Pari:")
    elif P1 == '1' and NCP == '2':
        print("Vince il PC:")
        cont2 += 1
    elif P1 == '2' and NCP == '3':
        print("Vince il PC:")
        cont2 += 1
    elif P1 == '3' and NCP == '1':
        print("Vince il PC:")
        cont2 += 1
    elif P1 == '1' and NCP == '3':
        print("Vinci tu:")
        cont1 += 1
    elif P1 == '2' and NCP == '1':
        print("Vinci tu:")
        cont1 += 1
    elif P1 == '3' and NCP == '2':
        print("Vinci tu:")
        cont1 += 1

    print(cont1, '-', cont2, sep="")

if cont1 > cont2:
    print("Hai vinto la sfida!")
else:
    print("Il PC ha vinto la sfida!")
