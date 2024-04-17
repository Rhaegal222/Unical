def main():
    costo_biglietto, tariffa = inserimento()
    listino = [0, 10, 15, 25]
    calcolo(costo_biglietto, tariffa, listino)

def inserimento():
    costo_biglietto = float(input())
    tariffa = int(input())
    return costo_biglietto, tariffa

def calcolo(costo_biglietto, tariffa, listino):
    costo_finale = costo_biglietto - ((costo_biglietto * listino[tariffa]) / 100)
    print(round(costo_finale, 3), end = '')

main()
