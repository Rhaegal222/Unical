import random, time
from threading import Thread, Lock
from sys import version

debug = False
def dprint(s):
    if debug:
        print(s)

class Striscia:
    LUNG = 50
    def __init__(self):
        self.striscia=list()
        self.fine = False
        self.dirGatto = 1
        self.topo = random.randint(0,self.LUNG-1)
        self.gatto = random.randint(0,self.LUNG-1)
        self.lockUnico = Lock()
        for i in range(0,self.LUNG):
                self.striscia.append( ' ' )
        self.striscia[self.topo] = '.'
        self.striscia[self.gatto] = '*'
        
    def printStriscia(self):
        with self.lockUnico:
            print (f"|{''.join(self.striscia)}|", end = '\r')
            return self.fine


    def muoviGatto(self): 
        with self.lockUnico:
            if not self.fine:
                self.striscia[self.gatto] = ' '
            
                if self.gatto + self.dirGatto > self.LUNG-1 or self.gatto + self.dirGatto < 0: 
                    self.dirGatto = -self.dirGatto

                self.gatto += self.dirGatto
                
                self.striscia[self.gatto] = '*'

                if  self.gatto == self.topo: 
                    self.fine = True
                    self.striscia[self.gatto] = '@'

            return self.fine


    def muoviTopo(self): 
        
        with self.lockUnico:

            if not self.fine:
                self.striscia[self.topo] = ' '
            
                self.salto = random.randint(-1,1)
                if  self.topo + self.salto >= 0 and self.topo + self.salto < self.LUNG:
                    self.topo = self.topo + self.salto
            
                self.striscia[self.topo] = '.'

                if self.gatto == self.topo:
                    self.fine = True
                    self.striscia[self.topo] = '@'
            
            return self.fine


class Display(Thread):

    def __init__(self,s):
        Thread.__init__(self)
        self.striscia = s
        
    def run(self):
        dprint ("First run Display")
        while not striscia.printStriscia():
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



print ("Start Gatto & Topo versione basic")
dprint ("Python version %s" % version)
striscia = Striscia()
jerry = Topo(striscia)
tom = Gatto(striscia)
telefunken = Display(striscia)
dprint ("Created Threads")
telefunken.start()
jerry.start()
tom.start()

dprint ("Threads started.")