mese = int(input())
if (mese < 1 or mese > 12):
    print("MESE NON VALIDO", end="")
else:
    if (mese >= 1 and mese < 3):
        print("INVERNO", end="")
    elif mese == 3:
        giorno = int(input())
        if (giorno >=1 and giorno <=20):
            print("INVERNO", end="")
        else:
            print("PRIMAVERA", end="")
    elif (mese > 3  and mese < 6):
        print("PRIMAVERA", end="")
    elif mese == 6:
        giorno = int(input())
        if (giorno >= 1 and giorno <= 20):
            print("PRIMAVERA", end="")
        else:
            print("ESTATE", end="")
    elif (mese > 6  and mese < 9):
        print("ESTATE", end="")
    elif mese == 9:
        giorno = int(input())
        if (giorno >= 1 and giorno <= 20):
            print("ESTATE", end="")
        else:
            print("AUTUNNO", end="")
    elif (mese > 9 and mese < 12):
        print("AUTUNNO", end="")
    elif mese == 12:
        giorno = int(input())
        if (giorno >= 1 and giorno <= 20):
            print("AUTUNNO", end="")
        else:
            print("INVERNO", end="")


