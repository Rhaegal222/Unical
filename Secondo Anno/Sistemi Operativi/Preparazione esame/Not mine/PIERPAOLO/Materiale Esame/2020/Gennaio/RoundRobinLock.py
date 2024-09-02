import random, time
from threading import RLock, Thread, Lock, Condition


class RoundRobinLock:

    def __init__(self, N : int):
        self.lock = RLock()
        self.condition = []
        for i in range (N): self.condition.append(Condition(self.lock))
        self.dim = N
        self.idInAttesa= []
        for i in range(N):
            self.idInAttesa.append(0)
        self.turnoCorrente = -1
        
        
    def acquire(self, id : int):
        with self.lock:
            while self.turnoCorrente != id and self.turnoCorrente != -1:
                self.idInAttesa[id] += 1
                self.condition[id].wait()
            
            self.idInAttesa[id] -= 1
            self.turnoCorrente = id
            self.condition[(id+1)%self.dim].notifyAll()



            

    def show(self): # mostra il contenuto del buffer
        
        self.lock.acquire()
        val = [None] * self.dim;
        
        for i in range(0,self.slotPieni):
            val[(self.out + i) % len(self.thebuffer)] = '*' # '*' indica che c'è un carattere
        
        for i in range(0,len(self.thebuffer) - self.slotPieni):
            val[(self.ins + i) % len(self.thebuffer)] = '-' # '-' indica che non c'è un carattere
        
        print("In: %d Out: %d C: %d" % (self.ins,self.out,self.slotPieni))
        print("".join(val))
        self.lock.release()


    def get(self): 

        self.lock.acquire()
        try:
            while self.slotPieni == 0:
                self.empty_condition.wait()
    
            returnValue = self.thebuffer[self.out]
            self.out = (self.out + 1) % len(self.thebuffer)
            
            self.full_condition.notifyAll()
            
            self.slotPieni -= 1
            return returnValue
        finally:
            self.lock.release()