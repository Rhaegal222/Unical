

import math
import multiprocessing
from threading import Condition, Lock, Thread
import time


class DistributoreNumeri:

    def __init__(self,min,max):
        self.min = min
        self.max = max
        self.numCorrente = min
        self.lock = Lock()
    '''
        Utilizzato dai macinatori per avere un numero da calcolare
    '''
    def getNextNumber(self):
        with self.lock:
            if self.numCorrente > self.max:
                return -1
            num = self.numCorrente
            self.numCorrente += 1
            return num


class Barrier:

    def __init__(self,n):

        self.soglia = n
        self.threadArrivati = 0
        self.lock = Lock()
        self.condition = Condition(self.lock)

    def wait(self):
        with self.lock:
            self.threadArrivati += 1

            if self.threadArrivati == self.soglia:
                self.condition.notify_all()

            while self.threadArrivati < self.soglia:
                self.condition.wait()

'''
    Utilizzabile per testare se un singolo numero è primo
'''
def eprimo(n):
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n)+1),2):
        if n % i == 0:
            return False
    return True

def isPrime(x):
    if x <= 3:
        return True
    if x % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(x)+1),2):
        if x % i == 0:
            return False
    return True

def countPrimes(begin,end):
    pass



'''
    Utilizzabile per conteggiare un singolo intervallo di numeri primi
'''
def contaPrimiSequenziale(min,max):
    totale = 0
    for i in range(min,max+1):
        if eprimo(i):
            totale += 1
    return totale

class Macinatore(Thread):
    def __init__(self,nome, d,b):
        super().__init__()
        self.name = nome
        self.min = min
        self.max = max
        self.totale = 0
        self.barrier = b
        self.distributore = d

    def getTotale(self):
        return self.totale
    
    def run(self):
        n = self.distributore.getNextNumber()
        quantiNeHoFatto = 0
        while(n != -1):
            
            if eprimo(n):
                self.totale += 1
            quantiNeHoFatto += 1
            n = self.distributore.getNextNumber()
        
        print(f"Il thread {self.name} ha finito e ha testato {quantiNeHoFatto} numeri")
        self.barrier.wait()

def contaPrimiMultiThread(min,max):

    nthread = multiprocessing.cpu_count()
    print(f"Trovato {nthread} processori" )
    ciucci = []
        
    b = Barrier(nthread+1)
    d = DistributoreNumeri(min,max)

    for i in range(nthread):
        ciucci.append(Macinatore(i, d, b ))
        ciucci[i].start()


    b.wait()

    totale = 0
    for i in range(nthread):
        totale += ciucci[i].getTotale()
    return totale



min = 100000    # 100_000
max = 1000000   # 1_000_000
start = time.time()
nprimi = contaPrimiMultiThread(min,max)
elapsed = time.time() - start
print (f"Primi tra {min} e {max}: {nprimi}")
print (f"Tempo trascorso: {elapsed} secondi")