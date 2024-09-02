from threading import Condition, Thread, RLock
from time import sleep
import random

class ContoBancario():
    def __init__(self):
        self.saldo=0
        self.lock= RLock()
        self.condition = Condition(self.lock)

    def deposita(self, importo):
        with self.lock:
            self.saldo += importo
            print(f"Deposito di {importo}€ effettuato. Saldo attuale: {self.saldo}€")


    def preleva(self, importo):
        with self.lock:
            if importo <= self.saldo:
                self.saldo -= importo
                print(f"Prelievo di {importo}€ effettuato. Saldo attuale: {self.saldo}€")
            else:
                print(f"Impossibile effettuare prelievo di {importo}€.")

    def controlla_saldo(self):
        with self.lock:
            print(f"Saldo attuale: {self.saldo}€")
    

class Correntista(Thread):
    def __init__(self, conto):
        super().__init__() 
        self.conto = conto
        self.controllore = Controllore(conto)

    def run(self):
        while True:
            azione = random.randint(1, 2)
            n = random.randint(1, 100)
            if azione == 1:
                self.conto.deposita(n)
            if azione == 2:
                self.conto.preleva(n)
            sleep(random.random())

class Controllore(Thread):
    def __init__(self, conto):
        super().__init__() 
        self.conto=conto

    def run(self):
        while True:
            self.conto.controlla_saldo()
            sleep(random.random())

if __name__ == "__main__":
    contoBancario= ContoBancario()
    
    for _ in range(5):
        thread = Correntista(contoBancario)
        thread.start()
        
    controllore = Controllore(contoBancario)
    controllore.start()
    