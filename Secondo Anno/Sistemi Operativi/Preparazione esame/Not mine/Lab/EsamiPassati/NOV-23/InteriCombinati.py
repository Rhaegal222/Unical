import BlockingQueue
import ReadWriteLockModificato
from threading import Thread,RLock, current_thread
from random import randint
import time


class InteriCombinati():
    def __init__(self):
        self.V = [ReadWriteLockModificato.DatoCondiviso(randint(1,100)) for i in range(10)]
    

    def calcola(self,i,j,op):
        # Acquisisci i lock in ordine crescente per evitare deadlock
        first, second = min(i, j), max(i, j)
        self.V[first].acquireReadLock()
        self.V[second].acquireReadLock()
        vi = self.V[i].getDato()
        vj = self.V[j].getDato()
        try:
            if op == '+':
                return vi + vj
            elif op == '-':
                return vi - vj
            elif op == '*':
                return vi * vj
            elif op == '/':
                return vi // vj if vj != 0 else -1
            elif op == '%':
                return vi % vj if vj != 0 else -1
        finally:
            self.V[second].releaseReadLock()
            self.V[first].releaseReadLock()
        

    def aggiorna(self,i,j,k,op):
        # Acquisisci tutti i lock necessari
        locks = sorted(set([i, j, k]))
        for idx in locks:
            if idx == k:
                self.V[idx].acquireWriteLock()
            else:
                self.V[idx].acquireReadLock()

        try:
            result = self.calcola(i,j,op)
            self.V[k].setDato(result)
            print(f"Thread {current_thread().name} aggiorna il dato in posizione {k} con il valore {result}")

        finally:
            for idx in reversed(locks):
                if idx == k:
                    self.V[idx].releaseWriteLock()
                else:
                    self.V[idx].releaseReadLock()
        

class Calcolatrice():
    def __init__(self,ic):
        self.ic = ic
        self.B=BlockingQueue.BlockingQueue(10)

        elaboratori=[Elaboratore(self.B,self.ic,i) for i in range(4)]
        produttori=[Produttore(self.B,i) for i in range(2)]
        
        for e in elaboratori:
            e.start()
        for p in produttori:
            p.start()

class Tupla():
    def __init__(self,i,j,k,op):
        self.i=i
        self.j=j
        self.k=k
        self.op=op

class Elaboratore(Thread):
    def __init__(self,B, IC, name):
        Thread.__init__(self)
        self.B=B
        self.IC=IC
        self.name=name

    def run(self):
        while True:
            tupla= self.B.get()
            self.IC.aggiorna(tupla.i,tupla.j,tupla.k,tupla.op)

class Produttore(Thread):
    def __init__(self,B,name):
        Thread.__init__(self)
        self.B=B
        self.name=name

    def run(self):
        while True:
            self.B.put(Tupla(randint(0,9),randint(0,9),randint(0,9),enum[randint(0,4)]))

enum = ['+','-','*','/', '%'] #con enum[i] si accede all'operatore i-esimo

def main():
    ic=InteriCombinati()
    Calcolatrice(ic)

if __name__ == '__main__':
    main()