
from threading import Thread, Condition, RLock
from random import randint
from time import sleep


NUMSTANZE = 2
MAXVISITE = 5
NUMMEDICI = 2
NUMVISITATORI = 25

ITERAZIONIDEITHREAD = 10

class RepartoOspedaliero():

    def __init__(self):
        #   stanze[i] = 1-5 se ci sono da 1 a 5 visitatori
        #   stanze[i] = -1 se c'è il medico
        #   stanze[i] = 0 se vuota
        self.stanze = [0 for i in range(NUMSTANZE+1)]
        self.lock = RLock()
        self.medico_wait = Condition(self.lock)
        self.visitatore_wait = Condition(self.lock)
    
    def entraMedicoInStanza(self, name, numero_stanza):
        self.lock.acquire()
        #print(f"[{name}] entra nel reparto")
        while self.stanze[numero_stanza] != 0:
            if(self.stanze[numero_stanza]==-1):
                print(f"[{name}] voleva entrare nella stanza {numero_stanza} ma c'è già un medico. Dunque aspetta.")
            else:
                print(f"[{name}] voleva entrare nella stanza {numero_stanza} ma ci sono visitatori. Dunque aspetta.")
            self.medico_wait.wait()

        self.stanze[numero_stanza] = -1
        print(f"[{name}] ENTRA nella stanza {numero_stanza} - valore = {self.stanze[numero_stanza]}")
        self.lock.release()

    def esceMedicoDaStanza(self, name, numero_stanza):
        self.lock.acquire()
        self.stanze[numero_stanza] = 0
        print(f"[{name}] ESCE dalla stanza {numero_stanza}: - valore = {self.stanze[numero_stanza]}")
        self.medico_wait.notify()
        self.visitatore_wait.notify()
        self.lock.release()

    def entraVisitatoreInStanza(self, name, numero_stanza):
        self.lock.acquire()
        #print(f"[{name}] entra nel reparto")
        while self.stanze[numero_stanza] == -1 or self.stanze[numero_stanza] > 4:
            if(self.stanze[numero_stanza]==-1):
                print(f"[{name}] voleva entrare nella stanza {numero_stanza} ma c'è già un medico. Dunque aspetta.")
            else:
                print(f"[{name}] voleva entrare nella stanza {numero_stanza} ma ci sono già 5 visitatori. Dunque aspetta.")
            self.visitatore_wait.wait()

        if(self.stanze[numero_stanza]<1):
            self.stanze[numero_stanza] = 1
        else:
            self.stanze[numero_stanza] += 1
        print(f"[{name}] ENTRA nella stanza {numero_stanza} - valore = {self.stanze[numero_stanza]}")
        self.lock.release()

    def esceVisitatoreDaStanza(self, name, numero_stanza):
        self.lock.acquire()
        self.stanze[numero_stanza] -= 1
        print(f"[{name}] esce dalla stanza {numero_stanza}: - valore = {self.stanze[numero_stanza]}")
        self.medico_wait.notify()
        self.visitatore_wait.notify()
        self.lock.release()

class Medico(Thread):

    def __init__(self, name, ro):
        super().__init__()
        self.name = name
        self.ro = ro
        
    def run(self):
        for i in range(ITERAZIONIDEITHREAD):
            stanza=randint(0,NUMSTANZE)
            self.ro.entraMedicoInStanza(self.name,stanza)
            sleep(0.1)
            self.ro.esceMedicoDaStanza(self.name,stanza)

class Visitatore(Thread):

    def __init__(self, name, ro):
        super().__init__()
        self.name = name
        self.ro = ro
        
    def run(self):
        for i in range(ITERAZIONIDEITHREAD):
            stanza=randint(0,NUMSTANZE)
            self.ro.entraVisitatoreInStanza(self.name,stanza)
            sleep(0.1)
            self.ro.esceVisitatoreDaStanza(self.name,stanza)



ro = RepartoOspedaliero()

for i in range(1,NUMMEDICI):
    newMedico=Medico(f"MEDICO {i}", ro)
    newMedico.start()

for i in range(1,NUMVISITATORI):
    newVisitatore=Visitatore(f"VISITATORE {i}", ro)
    newVisitatore.start()