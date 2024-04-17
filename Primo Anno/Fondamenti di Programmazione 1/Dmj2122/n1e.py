saldo = int(input())
canone = int(input())
interessi = int(input())
for i in ("PRIMO","SECONDO","TERZO"):
    print(str(i)+" MESE: " + str(round(saldo)),end="")
    saldo -= canone
    saldo *= ((interessi+100)/100)
    if(i != "TERZO"):
        print()