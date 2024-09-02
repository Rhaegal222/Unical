import random, time
from threading import Condition, RLock, Thread, Lock
from sys import version

debug = False
def dprint(s): #per le print di debug mettere debug = True
    if debug:
        print(s)

class Striscia: #è la risorsa condivisa
    LUNG = 50 #variabile di calsse, non è associata ad una particolare istanza, ma alla classe stessa, come le static di c++
    def __init__(self):
        self.striscia=list() #uguale a scrivere self.striscia=[]
        self.fine = False
        self.dirGatto = 1 # 1=verso destra, -1=verso sinistra
        self.topo = random.randint(0,self.LUNG-1)
        self.gatto = random.randint(0,self.LUNG-1)
        self.lockUnico = Lock()
        for i in range(0,self.LUNG):
                self.striscia.append( ' ' )
        self.striscia[self.topo] = '.'
        self.striscia[self.gatto] = '*'
        
    def printStriscia(self):
        with self.lockUnico:
            print (f"|{''.join(self.striscia)}|", end = '\r') #join() converte una lista in una stringa senza separatori di elementi
            return self.fine                                  #e \r torna a capo sulla stessa riga su cui si è appena stampato (usato per animazioni)


    def muoviGatto(self): 
        with self.lockUnico:
            if not self.fine:
                self.striscia[self.gatto] = ' '
            
                if self.gatto + self.dirGatto > self.LUNG-1 or self.gatto + self.dirGatto < 0: #il gatto quando arriva al bordo cambia direzione
                    self.dirGatto = -self.dirGatto

                self.gatto += self.dirGatto #si muove il gatto (dopo il controllo)
                
                self.striscia[self.gatto] = '*' #ricompare il gatto

                if  self.gatto == self.topo: #se lo acchiappa finisce il gioco
                    self.fine = True
                    self.striscia[self.gatto] = '@'

            return self.fine


    def muoviTopo(self): 
        
        with self.lockUnico:

            if not self.fine:
                self.striscia[self.topo] = ' '
            
                self.salto = random.randint(-1,1) #il topo si muove casualmente a destra, sinistra, o sta fermo
                if  self.topo + self.salto >= 0 and self.topo + self.salto < self.LUNG:
                    self.topo = self.topo + self.salto
            
                self.striscia[self.topo] = '.' #ricompare il topo

                if self.gatto == self.topo:
                    self.fine = True
                    self.striscia[self.topo] = '@'
            
            return self.fine

#
# Questa classe sincronizza meglio la funzione di stampa, che può avvenire solo dopo una modifica
# Può tuttavia ancora verificarsi che:
#  1. Il display fatica a prendere il lock e si perde una modifica consecutiva a un altra (sapreste perchè e come risolvere?)
#  2. Se il topo non si muove poichè sorteggia uno spostamento di 0, il display fa una stampa inutile in più (sapresti risolvere?)
#
class StrisciaMigliore(Striscia):

    def __init__(self):
        super().__init__()
        self.ceModifica = False
        #
        # Non posso più usare un Lock ma devo usare un RLock
        # Per cui sovrascrivo lockUnico
        #
        self.lockUnico = RLock() #in breve: RLock si usa quando si ha una ricorsione in una funzione lockata
        #
        # Introduco una condizione per il display
        #
        self.condDisplay = Condition(self.lockUnico)
       

    def printStriscia(self):
        #
        # N.B. il lock è già  acquisito ma mi serve un RLock per evitare che il programma si blocchi
        #
        with self.lockUnico:
            while not self.ceModifica and not self.fine:
                self.condDisplay.wait() #mentre aspetta il display si blocca e rilascia il lock 
            self.ceModifica = False
            return super().printStriscia() #per questo serve l'RLock, chiama printStriscia che è anch'essa lockata, col lock normale si bloccherebbe
    
    def muoviGatto(self): 
        with self.lockUnico:            
            self.ceModifica = True
            self.condDisplay.notify() #sveglia il thread (c'è solo Display) che devono stampare e che sono bloccati sulla wait al rigo 96 di printStriscia
            return super().muoviGatto()

    def muoviTopo(self):
        with self.lockUnico:
            self.ceModifica = True
            self.condDisplay.notify()
            return super().muoviTopo()


class Display(Thread):

    def __init__(self,s):
        Thread.__init__(self) 
        self.striscia = s
        
    def run(self):
        dprint ("First run Display")
        while not striscia.printStriscia(): #finchè non finisce il gioco (fine=true)
            time.sleep(0.020)
        striscia.printStriscia()
        print ("\nGioco Terminato")
        dprint ("Fine Display") 
    
class Gatto(Thread):

    def __init__(self,s):
        Thread.__init__(self)
        self.striscia = s

    def run(self):
        dprint ("First run Gatto")
        while not striscia.muoviGatto():
            time.sleep(0.100)
        dprint ("Fine Gatto")

class Topo(Thread):

    def __init__(self,s):
        Thread.__init__(self)
        self.striscia = s

    def run(self):
        dprint ("First run Topo")
        while not striscia.muoviTopo():
            time.sleep(0.050)
        dprint ("Fine Topo")

print ("Start Gatto & Topo")
dprint ("Python version %s" % version)

#
# Per avere la versione basic, usare Striscia
# Per avere la versione dove il display è sincronizzato, usare StrisciaMigliore
#
#striscia = Striscia()
striscia = StrisciaMigliore()
jerry = Topo(striscia)
tom = Gatto(striscia)
telefunken = Display(striscia)
dprint ("Created Threads")
telefunken.start()
jerry.start()
tom.start()

dprint ("Threads started.")