'''
Conto Bancario:
Progettare un’applicazione che simuli l’implementazione di un conto bancario, quindi programmare le classi
per la gestione delle operazioni di prelievo e deposito su un conto.

In particolare, si deve prevedere una classe ContoBancario che mette a disposizione operazioni per:

-   o depositare una certa somma sul conto o prelevare una somma dal conto (solo se la somma è disponibile, il conto non
    ammette la possibilità di andare "in rosso") o verificare il saldo corrente (cioè quanto c'è sul conto bancario allo stato attuale)

- una classe Correntista che è il thread autorizzato ad effettuare operazioni di deposito e prelievo sul ContoBancario

- una classe Controllore che è il thread autorizzato ad effettuare operazioni di controllo sul saldo attuale del conto

- un main che avvia l'applicazione, creando un ContoBancario, più threads di tipo Correntista che accedono allo stesso conto ed un thread di tipo Controllore.
'''

from random import random
from threading import Condition, Lock

from threading import Thread
from time import sleep


class ContoBancario:
    def __init__(self,saldo):
        self.saldo=saldo
        self.lock=Lock()

    def deposita (self, s):
        with self.lock:
            self.saldo+=s
            print(f"Deposito di {s}")

    def preleva (self,s):
        with self.lock:
            if self.saldo>=s:
                self.saldo-=s
                print(f"Prelievo di {s}")
            else:
                print(f"Impossibile prelevare {s}")

    def getSaldo (self):
        with self.lock:
            return self.saldo

class Correntista(Thread):
    def __init__(self,conto):
        super().__init__()
        self.conto=conto
    def run(self):
        while True:
            r=random()*100
            r=round(r,0)
            if random() > 0.5:
                self.conto.deposita(r)
            else:
                self.conto.preleva(r)
            sleep(random()*5)

class Controllore(Thread):
    def __init__(self,conto):
        super().__init__()
        self.conto=conto
    def run(self):
        while True:
            print(f"Il saldo attuale è {self.conto.getSaldo()}")
            sleep(random()*2)

def main():
    conto=ContoBancario(10)
    correntisti=[Correntista(conto) for i in range(5)]
    controllore=Controllore(conto)
    controllore.start()
    for c in correntisti:
        c.start()

if __name__ == "__main__":
    main()