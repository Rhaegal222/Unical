from threading import Thread, RLock
from time import sleep
import random

class Utilizzatore(Thread):
    def __init__(self, contatore):
        super().__init__()
        self.contatore = contatore
        self.c1=0
        self.c2=0
        self.c3=0

    def run(self):
        while self.c1<=3 and self.c2<=3 and self.c3<=3:
            with self.contatore.lock:
                azione = random.randint(1, 3)
                if azione == 1:
                    self.contatore.reset()
                    print(f"Reset: {self.contatore.c} Volta: {self.c1}")
                    self.c1+=1
                if azione == 2:
                    self.contatore.inc()
                    print(f"Incremento: {self.contatore.c} Volta: {self.c2}")
                    self.c2+=1
                if azione == 3:
                    self.contatore.dec()
                    print(f"Decremento: {self.contatore.c} Volta: {self.c3}")
                    self.c3+=1
            sleep(random.random())

class Contatore:
    def __init__(self):
        self.lock = RLock()
        self.c = 0

    def reset(self):
        with self.lock:
            self.c = 0

    def inc(self):
        with self.lock:
            self.c += 1

    def dec(self):
        with self.lock:
            self.c -= 1

if __name__ == "__main__":
    contatore = Contatore()

    threads = []
    for _ in range(5):
        thread = Utilizzatore(contatore)
        threads.append(thread)
        thread.start()
    
    for t in threads:
        t.join()
    
    print(f"\n Risultato totale: {contatore.c} \n Cicli: \n C1: {thread.c1} \n C2: {thread.c2} \n C3: {thread.c3} \n")