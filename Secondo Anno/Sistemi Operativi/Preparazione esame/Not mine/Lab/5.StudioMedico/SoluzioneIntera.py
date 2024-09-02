from threading import Condition, RLock
from threading import Thread
from random import randint, randrange, random
from time import sleep
from queue import Queue


##da ricetta
class Ricetta:
    lockRicetta=RLock()
    conditionRicetta=Condition(lockRicetta)
    medicina=None

    def attendiRicetta(self):
        self.lockRicetta.acquire()
        while(self.medicina==None):
            self.conditionRicetta.wait()
        self.lockRicetta.release()

    def ricettaPronta(self):
        self.lockRicetta.acquire()
        self.conditionRicetta.notify_all()
        self.lockRicetta.release()

##da paziente
class Paziente:
    nextIdPaziente=0 ##statico, codice paziente
    def __init__(self):
        self.nome="Paziente-"+str(Paziente.nextIdPaziente)
        self.ricetta=Ricetta()
        Paziente.nextIdPaziente+=1 ##cambia lo static, per tutti
        
        
##da genera pazienti
class PazienteRun(Thread):
    def __init__(self, salaDiAttesa):
        super().__init__()
        self.salaDiAttesa=salaDiAttesa

    def run(self):
        paziente = Paziente()

        n=random()

        if (n>0.5):  ##genera in modo random cosa deve fare il paziente
            self.salaDiAttesa.aggiungiPazienteVisita(paziente)
        else:
            self.salaDiAttesa.aggiungiPazienteRicetta(paziente)

        print("Il paziente " + paziente.nome + " è uscito con la ricetta " + paziente.ricetta.medicina)



class GeneraPazienti(Thread):  ##tgread che avvia i pazienti thread
    def __init__(self, salaDiAttesa):
        super().__init__()
        self.salaDiAttesa = salaDiAttesa

    def run(self):
        while(True):
            pazienteRun = PazienteRun(self.salaDiAttesa)
            pazienteRun.start()
            
            

##da medico
class Medico(Thread):
    def __init__(self, salaDiAttesa):
        super().__init__()
        self.salaDiAttesa=salaDiAttesa

    def run(self):
        while(True):
            p = self.salaDiAttesa.getPazienteVisita()
            n = random()

            sleep(randint(1,4))

            if (n>0.666666):
                p.ricetta.medicina="TUTTO OK"
                p.ricetta.ricettaPronta()
            elif(n>0.333333):
                p.ricetta.medicina="STAI BENE, PUOI ANDARE VIA SENZA RICETTA"
                p.ricetta.ricettaPronta()
            else:
                self.salaDiAttesa.aggiungiPazienteRicettaPrioritaria(p)
                
          
                
##da segretaria  
class Segretaria(Thread):
    def __init__(self, salaDiAttesa):
        super().__init__()
        self.salaDiAttesa=salaDiAttesa

    def run(self):
        while(True):
            p = self.salaDiAttesa.getProssimoPazienteRicetta()
            n = random()

            sleep(randint(1,4))


            if (n>0.666666):
                p.ricetta.medicina="MAALOX"
            elif(n>0.333333):
                p.ricetta.medicina="OKI"
            else:
                p.ricetta.medicina="AULIN"

            p.ricetta.ricettaPronta()



#da sala di attesa              
class SalaDiAttesa:

    lock = RLock()
    conditionTutteLeCodeVuote = Condition(lock)

    codaPazientiVisita = Queue()
    codaPazientiRicetta = Queue()
    codaPazientiRicettaPrioritaria = Queue()

    def aggiungiPazienteVisita(self, p):
        self.codaPazientiVisita.put(p)
        p.ricetta.attendiRicetta()
        return p.ricetta

    def aggiungiPazienteRicetta(self, p):
        self.codaPazientiRicetta.put(p)
        self.lock.acquire()
        self.conditionTutteLeCodeVuote.notify_all()
        self.lock.release()
        p.ricetta.attendiRicetta()
        return p.ricetta


    def aggiungiPazienteRicettaPrioritaria(self, p):
        self.codaPazientiRicettaPrioritaria.put(p)
        self.lock.acquire()
        self.conditionTutteLeCodeVuote.notify_all()
        self.lock.release()
        p.ricetta.attendiRicetta()
        return p.ricetta

    def getPazienteVisita(self):
        return self.codaPazientiVisita.get()

    def getProssimoPazienteRicetta(self):
        self.lock.acquire()
        try:
            while (self.codaPazientiRicettaPrioritaria.empty() and self.codaPazientiRicetta.empty()):
                self.conditionTutteLeCodeVuote.wait()

            if (not self.codaPazientiRicettaPrioritaria.empty()):
                return self.codaPazientiRicettaPrioritaria.get()
            else:
                return self.codaPazientiRicetta.get()
        finally:
            self.lock.release()


def main():
    salaDiAttesa = SalaDiAttesa()
    m = Medico(salaDiAttesa)
    s_1 = Segretaria(salaDiAttesa)
    s_2 = Segretaria(salaDiAttesa)
    gp = GeneraPazienti(salaDiAttesa)

    m.start()
    s_1.start()
    s_2.start()
    gp.start()

if __name__ == '__main__':
    main()