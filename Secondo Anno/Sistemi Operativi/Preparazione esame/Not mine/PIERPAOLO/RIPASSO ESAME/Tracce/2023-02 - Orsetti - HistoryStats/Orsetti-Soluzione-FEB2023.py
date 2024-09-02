import threading
import random
import time

class VasettoDiMiele:
    def __init__(self, indice, capacita):
        self.capacita = capacita
        self.miele = capacita   # quantità di miele presente inizializzata al max (capacita)
        self.indice = indice
        self.lock = threading.RLock()
        
        self.condition_aumento = threading.Condition(self.lock)
        self.condition_diminuzione = threading.Condition(self.lock)
        self.mamma_in_attesa = False

        self.quantitaMangiata = 0
        self.quantitaSospesa = 0

    #
    # Si sblocca solo quando il vasetto è totalmente vuoto
    #
    def riempi(self):
        with self.lock:
            while self.miele > 0 and self.miele != self.capacita:
                self.mamma_in_attesa = True
                print(f"Il vasetto {self.indice} ha ancora {self.miele} unità di miele, {threading.current_thread().name} aspetta che si svuoti completamente")
                self.condition_diminuzione.wait() ### in attesa di una diminuzione
            if(not(self.miele==self.capacita)):
                self.miele = self.capacita
                self.condition_aumento.notify_all() ### notificano un aumento
                print(f"{threading.current_thread().name} ha rabboccato il vasetto {self.indice}")

    def mangia(self, quantita):
        with self.lock:
            while self.miele < quantita: # se il miele da prendere è più di quanto ce n'è nel vasetto
                print(f"Il vasetto {self.indice} ha {self.miele} unità di miele, {threading.current_thread().name} non può prenderne {quantita}. Aspetto che il vasetto venga riempito")
                self.condition_aumento.wait() ### in attesa di un aumento
            self.miele -= quantita
            self.quantitaMangiata+=quantita
            print(f"Orsetto {threading.current_thread().name} ha mangiato {quantita} unità di miele dal vasetto {self.indice}")
            self.condition_diminuzione.notify_all() ### notificano una diminuzione

    #
    # Preleva del miele dal vasetto
    #
    def prendi(self, quantita):
        with self.lock:
            while self.miele < quantita: # se il miele da prendere è più di quanto ce n'è nel vasetto
                print(f"Il vasetto {self.indice} ha {self.miele} unità di miele, {threading.current_thread().name} non può prenderne {quantita}. Aspetto che il vasetto venga riempito")
                self.condition_aumento.wait() ### in attesa di un aumento
            self.miele -= quantita
            self.quantitaSospesa+=quantita
            print(f"Orso {threading.current_thread().name} ha preso {quantita} unità di miele dal vasetto {self.indice}")
            self.condition_diminuzione.notify_all() ### notificano una diminuzione

    def aggiungi(self, quantita):
        with self.lock:
            while (self.miele + quantita > self.capacita) or (self.mamma_in_attesa): # se il miele da aggiungere è troppo per la capacità del vasetto o se c'è una mamma che deve riempirlo
                if(self.miele + quantita > self.capacita):
                    print(f"Il vasetto {self.indice} ha {self.miele} unità di miele, {threading.current_thread().name} non può aggiungerne {quantita} supererebbe la capacità massima")
                else:
                    print(f"Mamma orso sta aspettando che il vasetto si svuoti per riempire, {threading.current_thread().name} deve aspettare")
                self.condition_diminuzione.wait()
            self.miele += quantita ### in attesa di una diminuzione
            self.quantitaSospesa-=quantita
            print(f"Orso {threading.current_thread().name} ha aggiunto {quantita} unità di miele al vasetto {self.indice}")
            self.condition_aumento.notify_all() ### notificano un aumento

    def getMiele(self):
        with self.lock:
            return self.miele


class OrsettoThread(threading.Thread):
    def __init__(self, name, vasettiMiele):
        threading.Thread.__init__(self)
        self.name = name
        self.vasettiMiele = vasettiMiele

    def run(self):
        while True:
            vasetto_indice = random.randint(0, len(self.vasettiMiele)-1)
            quantita = random.randint(1,self.vasettiMiele[vasetto_indice].capacita)
            self.vasettiMiele[vasetto_indice].mangia(quantita)

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


class Display(threading.Thread):
    def __init__(self, vasettiMiele):
        threading.Thread.__init__(self)
        self.vasettiMiele = vasettiMiele

    def totale_miele(self):
        sommaMielePresente = 0
        sommaMieleMangiato = 0
        sommaMieleFuoriVasetti = 0

        for i in range(len(self.vasettiMiele)):
            self.vasettiMiele[i].lock.acquire()
            
        for i in range(len(self.vasettiMiele)):
            sommaMielePresente += self.vasettiMiele[i].miele
            sommaMieleMangiato += self.vasettiMiele[i].quantitaMangiata
            sommaMieleFuoriVasetti += self.vasettiMiele[i].quantitaSospesa
            print(f"Nel vasetto {self.vasettiMiele[i].indice} ci sono {self.vasettiMiele[i].miele} grammi di miele.")

        print(f"\nIn tutti i vasetti c'è un totale di {sommaMielePresente} grammi di miele")
        print(f"I vasetti hanno mangiato fino ad ora {sommaMieleMangiato} grammi di miele")
        print(f"I papà hanno preso {sommaMieleFuoriVasetti} grammi di miele e stanno aspettando di aggiungerlo negli altri\n")
        
        for i in range(len(self.vasettiMiele)):
            self.vasettiMiele[i].lock.release()

    def run(self):
        while True:
            self.totale_miele()
            time.sleep(1) # Ogni quanto si vuole vedere la presenza di miele nei vasetti di miele




if __name__ == '__main__':
    num_vasetti = 5
    vasetti = [VasettoDiMiele(i,50+50*i) for i in range(num_vasetti)]


    orsetti = [OrsettoThread(f"Winnie-{i}", vasetti) for i in range(5)]
    mamme_orse = [MammaOrsoThread(f"Mamma-{i}",vasetti) for i in range(2)]
    papa_orso = [PapaOrsoThread(f"Babbo-{i}", vasetti) for i in range(3)]

    
    display = Display(vasetti)

    display.start()
 
    for orsetto in orsetti:
        orsetto.start()
 
    for orsa in mamme_orse:
        orsa.start()

    for orso in papa_orso:
        orso.start()

    
        
    
