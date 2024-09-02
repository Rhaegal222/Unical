from asyncio import threads
from threading import Thread, RLock, Condition
from time import sleep
import random

class Utilizzatore(Thread):
    def __init__(self, contatore):
        super().__init__()
        self.contatore = contatore

    def run(self):
        while True:
            azione = random.randint(1, 2)
            if azione == 1:
                self.contatore.inc()
                print(f"Incremento: {self.contatore.c}")
            if azione == 2:
                self.contatore.dec()
                print(f"Decremento: {self.contatore.c}")
            sleep(random.random())
                
class Azzeratore(Thread):
    def __init__(self, n, contatore):
        super().__init__()
        self.n = n
        self.contatore = contatore

    def run(self):
        while True:
            self.contatore.attendi(self.n)
 
class Contatore:
    def __init__(self):
        self.lock = RLock()
        self.c = 0
        self.condition = Condition(self.lock)
        self.conditionAzzeratore = Condition(self.lock)

    def reset(self):
        with self.lock:
            self.c = 0
            self.condition.notify()

    def inc(self):
        with self.lock:
            self.c += 1
            self.condition.notify()

    def dec(self):
        with self.lock:
            self.c -= 1
            self.condition.notify()
    
    def attendi(self, n):
        with self.lock:  
            while self.c != n:
                self.condition.wait()
            self.c = 0
            print("Contatore azzerato!")

if __name__ == "__main__":
    contatore = Contatore()

    utilizzatore = Utilizzatore(contatore)
    utilizzatore.start()

    azzeratore = Azzeratore(2, contatore)
    azzeratore.start()

    azzeratore2 = Azzeratore(-10, contatore)
    azzeratore2.start()
    