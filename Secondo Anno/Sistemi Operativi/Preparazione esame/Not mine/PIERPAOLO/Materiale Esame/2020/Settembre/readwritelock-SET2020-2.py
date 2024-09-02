from threading import Thread,RLock,Condition
from random import random
from time import sleep

#
# Funzione di stampa sincronizzata
#
plock = RLock()
def prints(s):
    plock.acquire()
    print(s)
    plock.release()

class DatoCondiviso():

    def __init__(self,v):
        self.dato = v
        self.numLettori = 0
        self.ceUnoScrittore = False
        self.lock = RLock()
        self.condition = Condition(self.lock)

    def getDato(self):
        return self.dato
    
    def setDato(self, i):
        self.dato = i


    def acquireReadLock(self):
        self.lock.acquire()
        while self.ceUnoScrittore:
            self.condition.wait()
        self.numLettori += 1
        self.lock.release()

    def releaseReadLock(self):
        self.lock.acquire()
        self.numLettori -= 1
        if self.numLettori == 0:
            self.condition.notify()
        self.lock.release()

    def acquireWriteLock(self):
        self.lock.acquire()
        while self.numLettori > 0 or self.ceUnoScrittore:
            self.condition.wait()
        self.ceUnoScrittore = True
        self.lock.release()

    def releaseWriteLock(self):
        self.lock.acquire()
        self.ceUnoScrittore = False
        self.condition.notify_all()
        self.lock.release()


class Scrittore(Thread):
    
    maxIterations = 1000

    def __init__(self, i, dc):
        super().__init__()
        self.id = i
        self.dc = dc
        self.iterations = 0

    def run(self):
        while self.iterations < self.maxIterations:
            prints("Lo scrittore %d chiede di scrivere." % self.id)
            self.dc.acquireWriteLock()
            prints("Lo scrittore %d comincia a scrivere." % self.id )
            sleep(random())
            self.dc.setDato(self.id)
            prints("Lo scrittore %d ha scritto." % self.id)
            self.dc.releaseWriteLock()
            prints("Lo scrittore %d termina di scrivere." % self.id)
            sleep(random() * 5)
            self.iterations += 1


class Lettore(Thread):
    maxIterations = 100

    def __init__(self, i, dc):
        super().__init__()
        self.id = i
        self.dc = dc
        self.iterations = 0

    def run(self):
        while self.iterations < self.maxIterations:
            prints("Il lettore %d Chiede di leggere." % self.id)
            self.dc.acquireReadLock()
            prints("Il lettore %d Comincia a leggere." % self.id)
            sleep(random())
            prints("Il lettore %d legge." % self.dc.getDato())
            self.dc.releaseReadLock()
            prints("Il lettore %d termina di leggere." % self.id)
            sleep(random() * 5)
            self.iterations += 1
  

if __name__ == '__main__':
        dc = DatoCondiviso(999)

        NUMS = 5
        NUML = 5
        scrittori = [Scrittore(i,dc) for i in range(NUMS)]
        lettori = [Lettore(i,dc) for i in range(NUML)]
        for s in scrittori:
            s.start()
        for l in lettori:
            l.start()


