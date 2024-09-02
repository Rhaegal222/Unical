from random import randrange
from threading import Lock, Thread
from time import sleep

class Bacchetta:

    def __init__(self):
        self.lock = Lock()
        #self.dato = 0

    def prendiBacchetta(self):
        self.lock.acquire()

    def lasciaBacchetta(self):
        self.lock.release()
'''
    def setDato(self,n):
            self.dato = n
    
    def getDato(self):
            return self.dato
'''   
class Tavolo:
    def __init__(self):
        self.bacchetta = [Bacchetta() for _ in range(5)] #lista di 5 bacchette

    def prendiTutteBacchette(self,pos):
        self.bacchetta[pos].prendiBacchetta()
        print(f"Il filosofo ha preso prima bacchetta.")
        self.bacchetta[(pos+1) % 5].prendiBacchetta()
        print(f"Il filosofo ha preso seconda bacchetta.")

    def lasciaTutteBacchette(self,pos):
        self.bacchetta[pos].lasciaBacchetta()
        print(f"Il filosofo ha lasciato la prima bacchetta.")
        self.bacchetta[(pos+1) % 5].lasciaBacchetta()
        print(f"Il filosofo ha lasciato la seconda bacchetta.")
   

class Filosofo(Thread):
     
    def __init__(self,tavolo,pos,nome):
          super().__init__()
          self.posizione = pos
          self.t = tavolo
          self.name = nome 
    
    def attendiACaso(self,msec):
         sleep(randrange(msec)/1000.0)

          

    def mangia(self):
        print(f"Il filosofo {self.name} vuole mangiare.")
        
        #self.t.bacchetta[self.posizione].prendiBacchetta()
        #print(f"Il filosofo {self.name} ha preso prima bacchetta.")
        #self.t.bacchetta[(self.posizione+1) % 5].prendiBacchetta()
        self.t.prendiTutteBacchette(self.posizione)
 
        print(f"Il filosofo {self.name} ha preso seconda bacchetta e comincia a mangiare.")

        #self.attendiACaso(300)

        print(f"Il filosofo {self.name} termina di mangiare.")
        
        self.t.lasciaTutteBacchette(self.posizione)
        
        #self.t.bacchetta[self.posizione].lasciaBacchetta()
        
        #print(f"Il filosofo {self.name} ha lasciato la prima bacchetta.")
        
        #self.t.bacchetta[(self.posizione+1) % 5].lasciaBacchetta()
        #print(f"Il filosofo {self.name} ha lasciato la seconda bacchetta.")
        
        
    def pensa(self):
        print(f"Il filosofo {self.name} pensa.")
        #self.attendiACaso(1000)
        print(f"Il filosofo {self.name} smette di pensare.")

    def run(self):
        while True:
             self.pensa()
             self.mangia()

nomi = ["Kant", "Fedez", "Crisippo", "Confucio", "Socrate"]

tavolo = Tavolo()

filosofi = [Filosofo(tavolo,i,nomi[i]) for i in range(5)]
for f in filosofi:
     f.start()