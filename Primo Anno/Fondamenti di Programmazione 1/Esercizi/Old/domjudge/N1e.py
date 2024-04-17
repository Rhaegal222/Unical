saldo = float(input())
canone = float(input())
interessi = float(input())

for i in ("PRIMO","SECONDO","TERZO"):
    print(str(i)+" MESE: " + str(round(saldo)),end="")
    saldo -= canone
    saldo *= 1+(interessi / 100)
    if(i != "TERZO"):
        print()