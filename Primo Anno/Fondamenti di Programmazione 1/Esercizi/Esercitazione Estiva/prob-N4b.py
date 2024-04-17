def main():
    costo_materiale = int(input())
    ore_lavorative = int(input())
    calcola(ore_lavorative, costo_materiale)

def calcola(ore_lavorative, costo_materiale):
    conto = (ore_lavorative * 40) + costo_materiale
    if conto <= 100:
        conto = 100
    print(conto, end='')
main()
