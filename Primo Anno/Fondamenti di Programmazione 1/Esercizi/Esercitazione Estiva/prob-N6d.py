def main():
    mese = int(input())
    stagioni = ['INVERNO', 'PRIMAVERA', 'ESTATE', 'AUTUNNO', 'INVERNO', 'MESE NON VALIDO']
    verifica(mese, stagioni)

def verifica(mese, stagioni):
    if mese >= 1 and mese < 4:
        stagione = 0
    elif mese >= 4 and mese < 7:
        stagione = 1
    elif mese >= 7 and mese < 10:
        stagione = 2
    elif mese >= 10 and mese < 13:
        stagione = 3
    else:
        stagione = 5
    if mese % 3 == 0:
        giorno = int(input())
        if giorno > 20:
            stagione += 1
    print(stagioni[stagione], end='')

main()
