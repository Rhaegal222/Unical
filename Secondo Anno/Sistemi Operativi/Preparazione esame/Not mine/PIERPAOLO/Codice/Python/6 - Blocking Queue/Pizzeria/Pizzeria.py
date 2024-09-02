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
  

O = 10
P = 10

class Pizzeria:
    def __init__(self):
        self.BOrdini = BlockingQueue(O)
        self.BPizze = BlockingQueue(P)

        self.lock = RLock()
        self.pizzamancante = Condition(self.lock)
        self.numOrdine=0

    def gen_id(self):
        #with self.lock:
        self.numOrdine += 1
        return self.numOrdine

    def putOrdine(self, codicePizza, quantita):
        tupla =(codicePizza, quantita)
        scontrino = self.gen_id()
        tupla += (scontrino, )
        self.BOrdini.put(tupla)
        return scontrino  
    
    def getOrdine(self):
        return self.BOrdini.get(0)

    def putPizza(self, pizza):          
        with self.lock:
            self.pizzamancante.notify_all()
            self.BPizze.put(pizza)
        
    def getPizza(self, riferimento):
        with self.lock:
            while True:
                for i in range(len(self.BPizze.elementi)):
                    if( self.BPizze.elementi[i][2] == riferimento ):
                        return self.BPizze.get(i)
                self.pizzamancante.wait()    

gusti_pizze = ("Margherita", "Diavola", "Quattro Stagioni", "Calabrese", "Marinara", "Bufalina")

class Cliente(Thread):

    def __init__(self, p, nome):
        super().__init__()
        self.name = nome
        self.pizzeria = p
        self.quantita = randint(1,20)
        self.codicePizza = randint(0,5)
        self.scontrino = -1

    def run(self):
        while (True):
            self.quantita = randint(1,20)
            self.codicePizza = randint(0,5)
            self.scontrino = self.pizzeria.putOrdine(self.codicePizza, self.quantita)
            with self.pizzeria.lock:
                print (f"Il cliente {self.name} ha ordinato {self.quantita} pizze {gusti_pizze[self.codicePizza]}")
            #sleep(0.5*self.quantita)
            pizza = self.pizzeria.getPizza(self.scontrino)
            with self.pizzeria.lock:
                print (f"Il cliente {self.name} ha ritirato {pizza[1]} pizze {gusti_pizze[self.codicePizza]}")

class Pizzaiolo(Thread):

    def __init__(self, p, nome):
        super().__init__()
        self.name = nome
        self.pizzeria = p

    def run(self):
        while (True):
            pizza=self.pizzeria.getOrdine()
            with self.pizzeria.lock:
                print (f"Il pizzaiolo {self.name} ha preso in carico {pizza[1]} pizze {gusti_pizze[pizza[0]]}")
            sleep(0.5*pizza[1]) 
            self.pizzeria.putPizza(pizza)
            with self.pizzeria.lock:
                print (f"Il pizzaiolo {self.name} dice che le {pizza[1]} {gusti_pizze[pizza[0]]} sono pronte")

Da_Toto = Pizzeria()

for i in range(10):
    newCliente = Cliente(Da_Toto, f"Cliente {i+1}")
    newCliente.start()
print("Clienti pronti\n")


for i in range(10):
    newPizzaiolo = Pizzaiolo(Da_Toto, f"Pizzaiolo {i+1}")
    newPizzaiolo.start()
print("Pizzaioli pronti\n")


