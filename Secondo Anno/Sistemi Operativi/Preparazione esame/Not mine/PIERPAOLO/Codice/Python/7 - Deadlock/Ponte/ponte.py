from threading import Thread,RLock,Condition
from random import randint
from time import sleep

from collections import deque

ITERAZIONIPRIMADISWITCHARE = 20

class Ponte():

    def __init__(self, size):
        self.conteggio = 0
        self.coda = deque()
        # 0 == montagna to mare
        # 1 == mare to montagna
        self.verso = 0
        self.lastverso = 0
        self.conteggiouguali = 0
        self.size = size
        self.lock = RLock()
        self.occupatoMontagna = Condition(self.lock)
        self.occupatoMare = Condition(self.lock)


    def entraMontagna(self, name):
        self.lock.acquire()
        if(self.conteggio == self.size):
            print(f"[{name}] voleva attraversare dal mare alla montagna ma trova che il ponte è pieno. Dunque aspetta.")
            self.occupatoMontagna.wait()
        #print(f"[{name}] prova a attraversare dal mare alla montagna")
        while (self.conteggio != 0 and self.verso != 1) or len(self.coda) == ITERAZIONIPRIMADISWITCHARE:
            print(f"[{name}] voleva attraversare dal mare alla montagna ma trova che il ponte è occupato da {self.verso}. Dunque aspetta.")
            self.occupatoMontagna.wait()
        if(self.conteggio==0):
            self.verso = 1
        self.conteggio += 1
        self.coda.append(name)
        print(f"[{name}] attraversa dal mare alla montagna")
        self.lock.release()
    
    def esciMontagna(self):
        self.lock.acquire()
        a=self.coda.popleft()
        print(f"[{a}] arrivato alla montagna")
        self.conteggio -= 1
        if(self.conteggio==0):
            self.occupatoMare.notify_all()
        self.lock.release()


    def entraMare(self, name):
        self.lock.acquire()
        if(self.conteggio == self.size):
            print(f"[{name}] voleva attraversare dalla montagna al mare ma trova che il ponte è pieno. Dunque aspetta.")
            self.occupatoMare.wait()
        #print(f"[{name}] prova a attraversare dalla montagna al mare")
        while (self.conteggio != 0 and self.verso != 0) or len(self.coda) == ITERAZIONIPRIMADISWITCHARE:
            print(f"[{name}] voleva attraversare dalla montagna al mare ma trova che il ponte è occupato da {self.verso}. Dunque aspetta.")
            self.occupatoMare.wait()
        if(self.conteggio==0):
            self.verso = 0
        self.conteggio += 1
        self.coda.append(name)
        print(f"[{name}] attraversa dalla montagna al mare")
        self.lock.release()
    
    def esciMare(self):
        self.lock.acquire()
        a=self.coda.popleft()
        print(f"[{a}] arrivato al mare")
        self.conteggio -= 1
        if(self.conteggio==0):
            self.occupatoMontagna.notify_all()
        self.lock.release()


class Auto(Thread):

    def __init__(self, nome, ponte, verso):
        super().__init__()
        self.name = nome
        self.ponte = ponte
        self.verso = verso


    def run(self):
        if(self.verso == 0):
            self.ponte.entraMare(self.name)
            #sleep(0.1)
            self.ponte.esciMare()
        else:
            self.ponte.entraMontagna(self.name)
            #sleep(0.1)
            self.ponte.esciMontagna()


ponte = Ponte(20)

for i in range(100 + 1):
    newAuto = Auto(f"Auto {i}", ponte, randint(0,1))
    newAuto.start()

