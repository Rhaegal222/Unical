from threading import Thread,RLock,Condition
from time import sleep
from random import randint,random

#
# Variabili e funzioni globali
#  
nomiDirezione = ["MARE","MONTAGNA"] 
    
# Ritorna la direzione opposta a quella passatagli come parametro
def opposta(direzione_corrente : int) -> int:
    
    return (direzione_corrente + 1) % 2


# DATO CONDIVISO
class PonteMareMonti: 

    # VARIABILI DI UTILITA' DELLA CLASSE
    MARE = 0 
    MONTAGNA = 1
    
    def __init__(self):
    
        self.direzionePonte = self.MARE
        self.turistiSulPonte = 0
    
        # VARIABILI PER GESTIONE THREAD
    
        self.lock = RLock()
        self.condition = Condition(self.lock)
    
        # VARIABILI PER LA GESTIONE DELLA STARVATION
        self.SOGLIA_GIRI = 3 # Non piÃ¹ di 3 turisti possono attraversare il
                             # ponte consecutivamente nella stessa direzione
        self.turisti_stessa_direzione_consecutivi = 0 # Conta il numero di turisti che hanno
                                                      # attraversato il ponte consecutivamente
                                                      # nella stessa direzione
        self.inAttesaPer = [0,0]
    
    # Il turista inizia l'attraversamento del ponte. Equivale a una sorta di takeLockSulPonte()
    def IniziaAttraversamentoPonte(self,direzione_turista : int, id_turista :int):
        with self.lock:
            self.inAttesaPer[direzione_turista] += 1
            while  ( (self.turistiSulPonte != 0 and self.direzionePonte != direzione_turista)  
                      or (self.direzionePonte == direzione_turista  
                          and self.turisti_stessa_direzione_consecutivi >= self.SOGLIA_GIRI 
                          and self.inAttesaPer[opposta(direzione_turista)] != 0)
                    ):
                self.condition.wait()
                
            self.inAttesaPer[direzione_turista] -= 1;
            
            if self.direzionePonte != direzione_turista:  #se cambio direzione resetto il contatore  
                self.direzionePonte = direzione_turista
                self.turisti_stessa_direzione_consecutivi = 0
            
            self.turisti_stessa_direzione_consecutivi += 1
            self.turistiSulPonte += 1;
            
            print("Il turista %d sta attaversando il Ponte in direzione: %s" % (id_turista,self.direzionePonte))
    

    # Il turista termina l'attraversamento del ponte
    def FinisciAttraversamentoPonte(self,id_turista : int):

        with self.lock:
        
            print("Il turista %d ha completato l'attraversamento !!!" % id_turista);
            
            self.turistiSulPonte -= 1
            if self.turistiSulPonte == 0:
                self.condition.notifyAll()
        
    
class Turista(Thread):

    def __init__(self,ponte : PonteMareMonti, id : int):
        super().__init__()
        self.ponte = ponte
        self.id = id;
        self.direzione = randint(0,1)
        print("Il turista %d vuole attraversare il ponte in direzione: %s" % (self.id,nomiDirezione[self.direzione]));
    
    
    
    def run(self):
        while True:
            self.ponte.IniziaAttraversamentoPonte(self.direzione, self.id)
            sleep(random())
            self.ponte.FinisciAttraversamentoPonte(self.id)

ponte = PonteMareMonti()
MAX_TURISTI = 10
turisti = [Turista(ponte,i+1) for i in range(MAX_TURISTI)]
for t in turisti:
    t.start()        
