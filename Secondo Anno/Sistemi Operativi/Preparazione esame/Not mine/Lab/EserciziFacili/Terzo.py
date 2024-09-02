'''
Estensione dell'esercizio 2.

Arricchire la classe "Contatore" di un metodo attendi(n) che rimane in attesa che il contatore raggiunga il valore "n" ricevuto come parametro. 

Modificare "Utilizzatore" in modo da fargli usare solo i metodi inc() e dec().

Definire un nuovo tipo di thread, "Azzeratore", che, scelto casualmente un valore n!=0, aspetti che il contatore raggiunga il valore n per poi
impostarlo a zero.
'''

from random import random
from threading import Condition, Lock, Thread
from time import sleep



class Contatore:
    def __init__(self):
        self.cont=0
        self.lock=Lock()
        self.cond=Condition(self.lock)

    def inc(self):
        with self.lock:
            self.cont+=1
            self.cond.notify()

    def dec(self):
        with self.lock:
            self.cont-=1
            self.cond.notify()

    def reset(self):
        with self.lock:
            self.cont=0
            self.cond.notify()
    
    def get(self):
        with self.lock:
            return self.cont

    def attendi(self,N):
        with self.lock:
            while self.cont!=N:
                self.cond.wait()

class Utilizzatore(Thread):
    def __init__(self, name, cont):
        super().__init__()
        self.name=name
        self.cont=cont
    def run(self):
        while True:
            print(f"{self.name} sta modificando il contatore")
            if random() > 0.5:
                self.cont.inc()
            else:
                self.cont.dec()
            
            print(f"{self.name} ha modificato il contatore, ora il contatore è {self.cont.get()}")
            sleep(random()*5)

class Azzeratore(Thread):
    def __init__(self, name, cont):
        super().__init__()
        self.name=name
        self.cont=cont
    def run(self):
        while True:
            N=0
            while N==0:
                N=int(random()*10)
            if random() > 0.5:
                N=-N
            print(f"{self.name} aspetta che il contatore raggiunga {N}")
            self.cont.attendi(N)
            self.cont.reset()
            print(f"{self.name} ha RESETTATO il contatore")

def main():
    cont= Contatore()
    utilizzatori= [Utilizzatore(f"Thread-{i}",cont) for i in range(5)]
    azzeratore= Azzeratore("Azzeratore",cont)
    azzeratore.start()
    for u in utilizzatori:
        u.start()

if __name__ == "__main__":
    main()