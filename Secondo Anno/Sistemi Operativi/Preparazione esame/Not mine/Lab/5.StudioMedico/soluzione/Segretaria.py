from threading import Thread
from random import random, randrange, randint
from time import sleep

class Segretaria(Thread):
    def __init__(self, salaDiAttesa):
        super().__init__()
        self.salaDiAttesa=salaDiAttesa

    def run(self):
        while(True):
            p = self.salaDiAttesa.getProssimoPazienteRicetta()
            n = random() # n è un numero casuale tra 0 e 1

            sleep(randint(1,4))


            if (n>0.666666):
                p.ricetta.medicina="MAALOX"
            elif(n>0.333333):
                p.ricetta.medicina="OKI"
            else:
                p.ricetta.medicina="AULIN"

            p.ricetta.ricettaPronta()





