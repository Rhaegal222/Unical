saldo = 500.0
for i in ("PRIMO","SECONDO","TERZO"):
    print(str(i)+" MESE: " + str(round(saldo)),end="")
    saldo -= 5.0
    saldo *= 1.02
    if(i != "TERZO"):
        print()