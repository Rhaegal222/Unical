from random import randrange
from threading import Lock, Thread
from time import sleep

'''Tutte e due le soluzioni, con e senza Lock'''
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
          self.bacchetta = [Bacchetta() for _ in range(5)] #crea un array di 5 oggetti bacchetta

class Filosofo(Thread):
     
    def __init__(self,tavolo,pos,nome):
          super().__init__()
          self.posizione = pos
          self.t = tavolo #stesso tavolo per tutti i filosofi
          self.name = nome 
    
    def attendiACaso(self,msec):
         sleep(randrange(msec)/1000.0) #pausa

    def mangia(self):
        print(f"Il filosofo {self.name} vuole mangiare.")
        
        self.t.bacchetta[self.posizione].prendiBacchetta() #acquire del lock (bacchetta sinistra)
        print(f"Il filosofo {self.name} ha preso prima bacchetta.")
        self.t.bacchetta[(self.posizione+1) % 5].prendiBacchetta() #acquire del lock (bacchetta destra)
        print(f"Il filosofo {self.name} ha preso seconda bacchetta e comincia a mangiare.")

        #self.attendiACaso(300) *mangia*

        print(f"Il filosofo {self.name} termina di mangiare.")
        self.t.bacchetta[self.posizione].lasciaBacchetta() #rilascia il lock della bacchetta di sinistra
        
        print(f"Il filosofo {self.name} ha lasciato la prima bacchetta.")
        
        self.t.bacchetta[(self.posizione+1) % 5].lasciaBacchetta() #rilascia il lock della bacchetta di destra
        print(f"Il filosofo {self.name} ha lasciato la seconda bacchetta.")
        
        
    def pensa(self):
        print(f"Il filosofo {self.name} pensa.")
        #self.attendiACaso(1000)
        print(f"Il filosofo {self.name} smette di pensare.")

    def run(self):
        while True:
             self.pensa()
             self.mangia()

class FilosofoNoDeadlock(Filosofo):
     
    def mangia(self):
        print(f"Il filosofo {self.name} vuole mangiare.")
        
        if self.posizione < (self.posizione +1) % 5: #per i primi 4 filosofi (pos=0..3) si prende la prima bacchetta a sinistra e la seconda a destra
             primaBacchetta = self.posizione
             secondaBacchetta = (self.posizione + 1) % 5
        else:                               #per l'ultimo filosofo (pos=4) si prende la prima bacchetta a destra e la seconda a sinistra (invertito)
             secondaBacchetta = self.posizione
             primaBacchetta = (self.posizione + 1) % 5

        self.t.bacchetta[primaBacchetta].prendiBacchetta()
        print(f"Il filosofo {self.name} ha preso prima bacchetta.")
        self.t.bacchetta[secondaBacchetta].prendiBacchetta()
        print(f"Il filosofo {self.name} ha preso seconda bacchetta e comincia a mangiare.")

        #self.attendiACaso(300)

        print(f"Il filosofo {self.name} termina di mangiare.")
        self.t.bacchetta[self.posizione].lasciaBacchetta()
        
        print(f"Il filosofo {self.name} ha lasciato la prima bacchetta.")
        
        self.t.bacchetta[(self.posizione+1) % 5].lasciaBacchetta()
        print(f"Il filosofo {self.name} ha lasciato la seconda bacchetta.")
 

nomi = ["Kant", "Fedez", "Crisippo", "Confucio", "Socrate"]

tavolo = Tavolo()

# Dichiarare i filosofi di tipo FilosofoNoDeadlock se si vuole evitare il deadlock
filosofi = [Filosofo(tavolo,i,nomi[i]) for i in range(5)]
for f in filosofi:
     f.start()