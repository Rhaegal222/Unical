IndicatoreSconto = {0:0,1:10,2:15,3:25}

Costo = float(input())
Sconto = int(input())

TotaleScontato = Costo - ((Costo*IndicatoreSconto[Sconto])/100)

print(round(TotaleScontato,3),end="")