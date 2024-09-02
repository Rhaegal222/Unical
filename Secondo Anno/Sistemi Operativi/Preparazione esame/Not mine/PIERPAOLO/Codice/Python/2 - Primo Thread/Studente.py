from Persona import Persona
from threading import Thread 
class Studente(Persona):
    matricole=0

    def __init__(self, cf, nome, cognome,eta):
        super().__init__(cf,nome,cognome,eta)
        Studente.matricole+=1
        self.matricola = Studente.matricole
        self.esami=[]

    def presentati(self):
        super().presentati()
        print(f"la mia matricola è {self.matricola}")
        for i in range(0,len(self.esami)):
            print(f"{self.esami[i].mat} {self.esami[i].voto} {self.esami[i].data}")

    def aggiungi_esame(self, esame):
        if esame.voto>24:
            self.esami.append(esame)

class Esame:

    def __init__(self,materia, data, voto):
        self.mat=materia
        self.data=data
        self.voto=voto


studenti = [Studente(f"jhfjhg{i}",f"ciccio{i}",f"pasticcio{i}",20+i) for i in range(10)]
for i in range(10):
    studenti[i].aggiungi_esame(Esame("SO", "15/06/2023",20+i))
    studenti[i].presentati()

print(Studente.matricole)