from threading import Thread
from random import random, randrange, randint
from time import sleep

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





