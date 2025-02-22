from Paziente import *
from threading import Thread
from random import randrange, random
'''3'''
class PazienteRun(Thread):
    def __init__(self, salaDiAttesa):
        super().__init__()
        self.salaDiAttesa=salaDiAttesa

    def run(self):
        paziente = Paziente()

        n=random() #valore casuale float da 0 a 1

        if (n>0.5):
            self.salaDiAttesa.aggiungiPazienteVisita(paziente)
        else:
            self.salaDiAttesa.aggiungiPazienteRicetta(paziente)

        print("Il paziente " + paziente.nome + " è uscito con la ricetta " + paziente.ricetta.medicina)



class GeneraPazienti(Thread):
    def __init__(self, salaDiAttesa):
        super().__init__()
        self.salaDiAttesa = salaDiAttesa

    def run(self):
        while(True):
            pazienteRun = PazienteRun(self.salaDiAttesa)
            pazienteRun.start()