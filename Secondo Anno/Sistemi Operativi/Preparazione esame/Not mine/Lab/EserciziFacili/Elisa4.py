from asyncio import threads
from threading import Condition, Thread, RLock
from time import sleep
import random
from typing import Mapping

class ContoBancario():
    def __init__(self):
        self.c=1000
        self.lock= RLock()
        self.condition = Condition(self.lock)

    def deposita(self,n):
        with self.lock:
            self.c+=n
            self.condition.notify()     

    def preleva(self,n):
        with self.lock:
            while self.c<n:             #faccio aspettare il thread finchè non ci sono abbastanza soldi sul conto
                self.condition.wait()
            self.c-=n
            self.condition.notify()      #tolta la notify() da preleva() perchè non ci sono thread in attesa che il saldo DIMINUISCA

    def saldoCorrente(self):
        with self.lock:     #messo il lock anche qui per evitare che il saldo venga modificato mentre lo si sta leggendo
            return (self.c)
    

class Correntista(Thread):
    def __init__(self, conto):
        super().__init__() 
        self.conto = conto
        #tolta l'istanza del controllore da qui e messa nel main

    def run(self):
        while True:
            azione = random.randint(1, 2)
            n = random.randint(1, 100)
            if azione == 1:
                self.conto.deposita(n)
            if azione == 2:
                #tolto il richiamo al run() di controllore
                self.conto.preleva(n)
            #tolta azione 3 perchè lo fa solo il controllore
            sleep(random.random())

class Controllore(Thread):
    def __init__(self, conto):
        super().__init__() #aggiunto super().__init__() per inizializzare il thread
        self.conto= conto

    def run(self,n):
            while True:
                print(f"Il saldo attuale è {self.conto.saldoCorrente()}") #ora fa solo il controllo del saldo ogni tot secondi
                sleep(random()*2)


def main():
    contoBancario= ContoBancario()
    controllore = Controllore(contoBancario) #aggiunto controllore nel main
    controllore.start()

    threads = []
    for _ in range(5):
        thread = Correntista(contoBancario)
        threads.append(thread)
        thread.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()