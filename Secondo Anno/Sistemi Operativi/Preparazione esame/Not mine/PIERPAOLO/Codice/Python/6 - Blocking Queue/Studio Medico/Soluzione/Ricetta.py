from threading import RLock, Condition

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
        self.conditionRicetta.notifyAll()
        self.lockRicetta.release()