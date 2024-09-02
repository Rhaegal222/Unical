from threading import RLock, Condition, Thread
from queue import Queue
from Medico import Medico
from Segretaria import Segretaria
from GeneraPazienti import GeneraPazienti


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
        self.conditionTutteLeCodeVuote.notifyAll()
        self.lock.release()
        p.ricetta.attendiRicetta()
        return p.ricetta


    def aggiungiPazienteRicettaPrioritaria(self, p):
        self.codaPazientiRicettaPrioritaria.put(p)
        self.lock.acquire()
        self.conditionTutteLeCodeVuote.notifyAll()
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