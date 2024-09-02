from threading import Condition, RLock, Thread
from time import sleep  
from random import randint   

class BlockingQueue:

    def __init__(self,size):

        self.elementi = []
        self.size = size
        self.lock = RLock()
        self.conditionTuttoPieno = Condition(self.lock)
        self.conditionTuttoVuoto = Condition(self.lock)

    def put(self,t):
        with self.lock:
            while len(self.elementi) == self.size:
                self.conditionTuttoPieno.wait()
            if len(self.elementi) == 0:
                self.conditionTuttoVuoto.notify()
            self.elementi.append(t)

    def get(self, index):
        with self.lock:
            while len(self.elementi) == 0:
                self.conditionTuttoVuoto.wait()
            if len(self.elementi) == self.size:
                self.conditionTuttoPieno.notify()
            return self.elementi.pop(index)
        
    def getLunghezza(self):
        return len(self.elementi) 

# Posti nella sala d'attesa
POSTI = 10

class Studiomedico:

    def __init__(self):
        self.Battesa = BlockingQueue(POSTI)
        self.BRicetta = BlockingQueue(POSTI)
        self.BPrioritaria = BlockingQueue(POSTI)

        self.lock = RLock()
        self.studioVuoto = Condition(self.lock)
        self.studioPieno = Condition(self.lock)

    def putPazienteInAttesa(self, tupla):

        self.Battesa.put(tupla)

    def putPaziente(self, tupla):
        if(tupla[1]==1):                
            self.BPrioritaria.put(tupla)
        elif(tupla[1]==0):            
            self.BRicetta.put(tupla)
        else:
            print("Tipo di visita non valido, inserire un tipo valido")

    def getPaziente(self):
        return self.Battesa.get(0)

    def getPazienteRicetta(self):
        while True:
            if self.BPrioritaria.elementi:
                return self.BPrioritaria.get(0)
            elif self.BRicetta.elementi:
                return self.BRicetta.get(0)

tipo_Visita = ("Visita","Ricetta","Ricetta Prioritaria")

class Paziente(Thread):

    def __init__(self, s, name, tipoVisita):
        super().__init__()
        self.studioMedico = s
        self.name = name
        self.tipoVisita = tipoVisita

    def run(self):
        # tupla[0] = nome
        # tupla[1] = tipovisita
        tupla =(self.name, self.tipoVisita)
        self.studioMedico.putPazienteInAttesa(tupla)
        
        with self.studioMedico.lock:
            print(f"[PAZIENTE {self.name}] in attesa per {tipo_Visita[self.tipoVisita]}")

        # tupla: "nome paziente", "tipo di visita"
        # 0 = Visita
        # 1 = Ricetta        
        # 2 = Ricetta Prioritaria

class Medico(Thread):

    def __init__(self, s):
        super().__init__()
        self.studioMedico = s

    def run(self):
        while True:
            tupla = self.studioMedico.getPaziente()
            #with self.studioMedico.lock:
            
            with self.studioMedico.lock:
                print(f"[MEDICO] ha fatto entrare il paziente {tupla[0]}.")
            if(tupla[1]==0):    # se ha fatto una visita
                
                with self.studioMedico.lock:
                    print(f"[MEDICO] sta visitando il paziente {tupla[0]}.")
                #sleep(1) # tempo di visitare
                if(randint(0,2)==0):    # scegliere casualmente se è necessaria la ricetta
                    self.studioMedico.putPaziente(tupla)
                    
                with self.studioMedico.lock:
                    print(f"[MEDICO] paziente {tupla[0]} visitato, può essere dimesso.")
            elif(tupla[1]==1): # se è venuto per una ricetta
                self.studioMedico.putPaziente(tupla)   
                
                with self.studioMedico.lock: 
                    print(f"[MEDICO] manda il paziente {tupla[0]} dalla segretaria per la ricetta.")

class Segretaria(Thread):

    def __init__(self, s):
        super().__init__()
        self.studioMedico = s

    def run(self):
        while(True):
            tupla = self.studioMedico.getPazienteRicetta()
            with self.studioMedico.lock:
                print(f"[SEGRETARIA] ricetta consegnata al paziente {tupla[0]}.")


s = Studiomedico()

medico = Medico(s)
segretaria = Segretaria(s)

medico.start()
print("medico pronto")

segretaria.start()
print("segretaria pronto")

for i in range(10):
    newPaziente = Paziente(s, f"{i+1}", randint(0,1))
    newPaziente.start()
print("pazienti pronti")