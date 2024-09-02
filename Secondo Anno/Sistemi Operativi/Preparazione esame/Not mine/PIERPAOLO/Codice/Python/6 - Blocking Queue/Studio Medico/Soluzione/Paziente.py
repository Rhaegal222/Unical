from Ricetta import Ricetta

class Paziente:
    nextIdPaziente=0
    def __init__(self):
        self.nome="Paziente-"+str(Paziente.nextIdPaziente)
        self.ricetta=Ricetta()
        Paziente.nextIdPaziente+=1