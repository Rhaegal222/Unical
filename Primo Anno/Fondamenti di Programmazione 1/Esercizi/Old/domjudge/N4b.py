costoorario = 40
costominimo = 100

CostoMateriale = int(input())
OreLavorative = int(input())

if( OreLavorative * costoorario + CostoMateriale >= 100.0):
    print(OreLavorative * costoorario + CostoMateriale, end="")
else:
    print(100, end="")
