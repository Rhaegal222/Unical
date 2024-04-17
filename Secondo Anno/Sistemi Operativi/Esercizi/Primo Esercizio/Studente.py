from Persona import Persona
from Esame import Esame

class Studente(Persona):
    listaEsami = [Esame("SOR", 12, 21), Esame("SIW", 6, 30)]
    def __init__(self, **kwargs):
        if 'matricola' in kwargs:
            self.matricola = kwargs['matricola']

        super(Studente, self).__init__(**kwargs)
        #super().__init__(**kwargs)

    def print(self):
        super().print()
        print("Matricola:\t %s" % (self.matricola))

    def addEsame(self, esame):
        self.listaEsami.append(esame)

    def printListaEsami(self):
        for e in self.listaEsami:
            e.print()

    def calcolaMedia(self):
        sommaCFU=0
        numeratore=0
        for e in self.listaEsami:
            sommaCFU+=e.cfu
            numeratore+=e.voto * e.cfu

        return (numeratore/sommaCFU)

    def controllaEsame(self, esame):
        if esame in self.listaEsami:
            return True
        return False