import threading
import random

class VasettoDiMiele:
    def __init__(self, indice, capacita):
        self.capacita = capacita
        self.miele = capacita
        self.indice = indice
        self.lock = threading.RLock()
        self.condition = threading.Condition(self.lock)

    #
    # Si sblocca solo quando il vasetto è totalmente vuoto
    #
    def riempi(self):
        with self.lock:
            while self.miele > 0:
                print(f"Il vasetto {self.indice} ha {self.miele} unità di miele, aspetto che si svuoti completamente")
                self.condition.wait()
            self.miele = self.capacita
            self.condition.notify_all()
            print(f"{threading.current_thread().name} ha rabboccato il vasetto {self.indice}")

    #
    # Preleva del miele dal vasetto
    #
    def prendi(self, quantita):
        with self.lock:
            while self.miele < quantita:
                print(f"Il vasetto {self.indice} ha {self.miele} unità di miele, non è possibile prendere {quantita}. Aspetto che il vasetto venga riempito")
                self.condition.wait()
            self.miele -= quantita
            print(f"Orsetto {threading.current_thread().name} ha preso {quantita} unità di miele dal vasetto {self.indice}")
            self.condition.notify_all()

    def aggiungi(self, quantita):
        with self.lock:
            while self.miele + quantita > self.capacita:
                print(f"Il vasetto {self.indice} ha {self.miele} unità di miele, aggiungerne {quantita} supererebbe la capacità massima di {self.capacita}")
                self.condition.wait()
            self.miele += quantita
            print(f"Orso {threading.current_thread().name} ha aggiunto {quantita} unità di miele al vasetto {self.indice}")
            self.condition.notify_all()


class OrsettoThread(threading.Thread):
    def __init__(self, name, vasettiMiele):
        threading.Thread.__init__(self)
        self.name = name
        self.vasettiMiele = vasettiMiele

    def run(self):
        while True:
            vasetto_indice = random.randint(0, len(self.vasettiMiele)-1)
            quantita = random.randint(1,self.vasettiMiele[vasetto_indice].capacita)
            self.vasettiMiele[vasetto_indice].prendi(quantita)

class PapaOrsoThread(threading.Thread):
    def __init__(self, name, vasettiMiele):
        threading.Thread.__init__(self)
        self.name = name
        self.vasettiMiele = vasettiMiele

    def run(self):
        while True:
            vasetto_indice1 = random.randint(0, len(self.vasettiMiele)-1)
            vasetto_indice2 = random.randint(0, len(self.vasettiMiele)-1)
            while vasetto_indice1 == vasetto_indice2:
                vasetto_indice2 = random.randint(0, len(self.vasettiMiele)-1)
            quantita = random.randint(1, self.vasettiMiele[vasetto_indice1].capacita)
            self.vasettiMiele[vasetto_indice1].prendi(quantita)
            self.vasettiMiele[vasetto_indice2].aggiungi(quantita)
            print(f"Papa orso {self.name} ha spostato {quantita} grammi dal vasetto {vasetto_indice1} al vasetto {vasetto_indice2}")

class MammaOrsoThread(threading.Thread):
    def __init__(self, name, vasettiMiele):
        threading.Thread.__init__(self)
        self.name = name
        self.vasettiMiele = vasettiMiele

    def run(self):
        while True:
            vasetto_indice = random.randint(0, len(self.vasettiMiele)-1)
            self.vasettiMiele[vasetto_indice].riempi()
            print(f"Mamma orso {self.name} ha riempito il vasetto {vasetto_indice}")


if __name__ == '__main__':
    num_vasetti = 5
    vasetti = [VasettoDiMiele(i,50+50*i) for i in range(num_vasetti)]

    orsetti = [OrsettoThread(f"Winnie-{i}", vasetti) for i in range(5)]
    mamme_orse = [MammaOrsoThread(f"Mamma-{i}",vasetti) for i in range(2)]
    papa_orso = [PapaOrsoThread(f"Babbo-{i}", vasetti) for i in range(3)]

 
    for orsetto in orsetti:
        orsetto.start()
 
    for orsa in mamme_orse:
        orsa.start()

    for orso in papa_orso:
        orso.start()
        
    
