from threading import RLock, Condition
'''1'''
class Ricetta:
    lockRicetta=RLock()
    conditionRicetta=Condition(lockRicetta)
    medicina=None
    #ponendo il caso tutti i pazienti aspettano che sia disponibile la stessa medicina
    def attendiRicetta(self):
        self.lockRicetta.acquire()
        while(self.medicina==None): #mentre medicina=false aspetta
            self.conditionRicetta.wait()
        self.lockRicetta.release()

    def ricettaPronta(self): #se la ricetta è pronta sveglia tutti
        self.lockRicetta.acquire()
        self.conditionRicetta.notifyAll()
        self.lockRicetta.release()