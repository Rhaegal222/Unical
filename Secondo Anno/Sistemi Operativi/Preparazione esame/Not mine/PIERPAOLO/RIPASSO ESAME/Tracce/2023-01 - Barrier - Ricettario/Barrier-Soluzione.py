

import math
import multiprocessing
from threading import Condition, Lock, Thread, RLock
import time 


class Barrier:
    def __init__(self,n):
        self.soglia = n
        self.threadArrivati = 0
        self.lock = RLock()
        self.condition = Condition(self.lock)

    def wait(self):
        with self.lock:
            self.threadArrivati += 1

            if self.threadArrivati == self.soglia:
                self.condition.notify_all()

            while self.threadArrivati < self.soglia:
                self.condition.wait()


class ExtendedBarrier(Barrier):
    def __init__(self, n):
        super().__init__(n)



    def finito(self):
        with self.lock:
            self.threadArrivati+=1

    def aspettaEbasta(self):
        with self.lock:
            while self.threadArrivati < self.soglia:
                self.condition.wait()

    def wait(self):
        with self.lock: #SERVE RLOCK
            self.finito()
            self.aspettaEbasta()
            if self.threadArrivati == self.soglia:
                self.condition.notify_all()


class DoppiaBarriera:
    def __init__(self, n0, n1):
        self.s0 = n0
        self.s1 = n1
        self.threadArrivati0 = 0
        self.threadArrivati1 = 0
        self.lock = RLock()
        self.condition0 = Condition(self.lock)
        self.condition1 = Condition(self.lock)

    def finito(self, numSoglia):
        with self.lock:
            if(numSoglia == 0):
                self.threadArrivati0 += 1
            elif(numSoglia == 1):
                self.threadArrivati1 += 1

    def aspettaEbasta(self, numSoglia):
        with self.lock:
            if(numSoglia == 0):
                while self.threadArrivati0 < self.s0:
                    self.condition0.wait(0)
            elif(numSoglia == 1):
                while self.threadArrivati1 < self.s1:
                    self.condition1.wait(1)

    def wait(self, numSoglia):
        with self.lock:
            self.finito(numSoglia)
            self.aspettaEbasta(numSoglia)
            if(numSoglia == 0):
                if self.threadArrivati0 == self.s0:
                    self.condition0.notify_all()
            elif(numSoglia == 1):
                if self.threadArrivati1 == self.s1:
                    self.condition1.notify_all()

    def waitAll(self):
        with self.lock:
            self.finito(0)
            self.finito(1)
            self.aspettaEbasta(0)
            self.aspettaEbasta(1)

            if (self.threadArrivati0 == self.s0) and (self.threadArrivati1 == self.s1):

                    self.condition0.notify_all()
                    self.condition1.notify_all()


class Stampatore(Thread):
    def __init__(self, barrier, nome):
        super().__init__()
        self.stringa = "*"
        self.name = nome
        self.barrier = barrier

    def run(self):
        while True:
            print(f"{self.name}: {self.stringa}\n")
            self.barrier.wait()

class StampatoreDoubleWait(Thread):
    def __init__(self, double_barrier, nome, num_soglia):
        super().__init__()
        self.stringa = "*"
        self.name = nome
        self.double_barrier = double_barrier
        self.num_soglia = num_soglia

    def run(self):
        while True:
            time.sleep(2)
            print(f"{self.name}: {self.stringa}\n")
            self.double_barrier.wait(self.num_soglia)

class StampatoreDoubleWaitAll(Thread):
    def __init__(self, double_barrier, nome, num_soglia):
        super().__init__()
        self.stringa = "*"
        self.name = nome
        self.double_barrier = double_barrier
        self.num_soglia = num_soglia

    def run(self):
        while True:
            print(f"{self.name}: {self.stringa}\n")
            self.double_barrier.waitAll()



# FARE MAIN

if __name__ == '__main__':


    NTHREAD = 5
    s0 = NTHREAD
    s1 = 3

    ''' # SOLUZIONE EXTENDED BARIER

    extendedBarrier = ExtendedBarrier(s0) # arriva a 5
    stampatore = [Stampatore(extendedBarrier, _+1) for _ in range(NTHREAD)]
    for s in stampatore:
        s.start()

    '''

    ''' # SOLUZIONE DoppiaBarriera col wait

    doppiaBarriera = DoppiaBarriera(s0,s1)     # arriva a 8  
    stampatore = [StampatoreDoubleWait(doppiaBarriera, _+1,s0) for _ in range(NTHREAD)]
    stampatore2 = [StampatoreDoubleWait(doppiaBarriera, _+1+NTHREAD,s1) for _ in range(s1)]

    for s in stampatore:
        s.start()
    for s in stampatore2:
        s.start()
        
    ''' 

    ''' # SOLUZIONE DoppiaBarriera col waitAll

    doppiaBarriera = DoppiaBarriera(s0,s1)     # arriva a 8  
    stampatore = [StampatoreDoubleWait(doppiaBarriera, _+1,s0) for _ in range(NTHREAD)]
    stampatore2 = [StampatoreDoubleWait(doppiaBarriera, _+1+NTHREAD,s1) for _ in range(s1)]

    for s in stampatore:
        s.start()
    for s in stampatore2:
        s.start()

    ''' 



            







