Calls = int(input())

PrimaTariffa = 5
SecondaTariffa = PrimaTariffa + (Calls - 80)*0.10
TerzaTariffa = 11 + (Calls - 140)*0.07
QuartaTariffa = 14.5 + (Calls - 190)*0.05

if Calls <= 80:
    print(round(PrimaTariffa,3), end="")
elif Calls > 80 and Calls <= 140:
    print(round(SecondaTariffa, 3), end="")
elif Calls > 140 and Calls <= 190:
    print(round(TerzaTariffa, 3), end="")
else:
    print(round(QuartaTariffa, 3), end="")