'''
Si vogliono sincronizzare dei threads di tipo "Utilizzatore" sull'utilizzo di una struttura dati condivisa di tipo "Contatore".
In particolare, si deve definire:

una classe Contatore che fornisce i metodi necessari per gestire un contatore. Le operazioni possibili sono reset()
(imposta il contatore a zero), inc() (aumenta il contatore di 1) e dec() (decrementa il contatore di 1).
I metodi pubblici del Contatore devono essere Thread-Safe. 

un tipo di thread Utilizzatore, che ad intervalli casuali modifica il valore del contatore usando i metodi di quest'ultimo
'''

from threading import Lock, Thread
from random import random
from time import sleep

class Contatore:
    def __init__(self):
        self.cont=0
        self.lock=Lock()

    def inc(self):
        with self.lock:
            self.cont+=1

    def dec(self):
        with self.lock:
            self.cont-=1
    def reset(self):
        with self.lock:
            self.cont=0
    
    def get(self):
        with self.lock:
            return self.cont


class Utilizzatore(Thread):
    def __init__(self, name, cont):
        super().__init__()
        self.name=name
        self.cont=cont
    def run(self):
        while True:
            print(f"Il Thread {self.name} sta modificando il contatore")
            if random() > 0.5:
                self.cont.inc()
            else:
                self.cont.dec()
            
            if random() > 0.8:
                self.cont.reset()
            
            print(f"{self.name} ha modificato il contatore, ora il contatore è {self.cont.get()}")
            sleep(random()*5)

def main():
    cont= Contatore()
    utilizzatori= [Utilizzatore(f"Thread-{i}",cont) for i in range(5)]
    for u in utilizzatori:
        u.start()

if __name__ == "__main__":
    main()