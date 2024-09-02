from Ricetta import Ricetta
'''2'''
class Paziente:
    nextIdPaziente=0 #var. statica
    def __init__(self):
        self.nome="Paziente-"+str(Paziente.nextIdPaziente)
        self.ricetta=Ricetta() #ogni paziente ha un'istanza diversa di Ricetta
        Paziente.nextIdPaziente+=1