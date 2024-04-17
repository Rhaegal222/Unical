class CashRegister:
    #inizializzo la classe
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0

    #funzione per aggiungere un singolo prodotto
    def addItem(self, price):
        self._itemCount += 1
        self._totalPrice += price
    
    #funzione per aggiungere piú prodotti
    def addItems(self, quantity, price):
        for i in range(quantity):
            self.addItem(price)

    #funzione per ottenere il totale
    def getTotal(self):
        return self._totalPrice

    #funzione per ottenere il numero di prodotti
    def getCount(self):
        return self._itemCount

    #funzione per ottenere cancellare prodotti e prezzi
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0

#dichiarazione dell'oggetto
register1 = CashRegister()

#utilizzo della funzione membro sull'oggetto
register1.addItems(6, 0.95)

print('Numero di articoli:', register1.getCount())
print('Totale:', register1.getTotal())