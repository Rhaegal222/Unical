import queue
from random import randint
from threading import Condition, Thread,Lock
from time import sleep

#risorse condivise (BO e BP)

#BO è FIFO ed ha istanze di tipo <codicePizza,quantita> in cui codicePizza è 0:Margherita, 1:Quattro Formaggi etc
class BO():
    def __init__(self, O):
        self.dim = O
        self.BO = queue.Queue(self.dim)
        self.lockBO = Lock()
        self.condBO = Condition(self.lockBO)
    
    def putOrdine(self, codicePizza, quantita):
        ordine = Ordine(codicePizza, quantita)
        with self.lockBO:
            while self.BO.full():
                self.condBO.wait()
            self.BO.put(ordine)
        return ordine
    
    def getOrdine(self):
        with self.lockBO:
            while self.BO.empty():
                self.condBO.wait()
            ordine = self.BO.get()
        return ordine
    
#BP non è FIFO e ha il metodo getPizze che preleva le pizze pronte
#e putPizze che mette le pizze pronte
class BP():
    def __init__(self, P):
        self.dim = P
        self.BP = [None]*self.dim
        self.lockBP = Lock()
        self.condBP = Condition(self.lockBP)
    
    def putPizze(self, codicePizza, quantita):
        ordine = Ordine(codicePizza, quantita)
        with self.lockBP:
            while len(self.BP):
                self.condBP.wait()
            self.BP.put(ordine)
        return ordine
    
    def getPizze(self):
        with self.lockBP:
            while self.BP.empty():
                self.condBP.wait()
            ordine = self.BP.get()
        return ordine

class Ordine():
    def __init__(self, CP, Q):
        self.codicePizza = CP
        self.quantita = Q

#thread che mette in BO un ordine tramite il metodo putOrdine, del tipo <codicePizza, quantita>
#e tramite getPizze preleva le pizze pronte
class Cliente(Thread):
    def __init__(self, BO, BP):
        super().__init__()
        self.BO = BO
        self.BP = BP
    def run(self):
        while True:
            sleep(0.1)
            CP= randint(5)
            Q = randint(10)
            BO.putOrdine(CP,Q)
            print(f"Cliente {self.name} ha ordinato {Q} pizze di tipo {enum[CP]}")
            sleep(0.2*Q)
            BP.getPizze()

#thread che preleva da BO tramite getOrdine, e tramaite putPizze mette in BP le pizze pronte
class Pizzaiolo(Thread):
    def __init__(self, BO, BP):
        super().__init__()
        self.BO = BO
        self.BP = BP
    def run(self):
        while True:
            self.getOrdine()
            self.putPizze()

enum = {'Margherita':0, 'Quattro Formaggi':1, 'Diavola':2, 'Viennese':3, 'Bufalina':4, 'Marinara':5}

class Pizzeria():
    def __init__(self, O, P, NC, NP):
        self.BO = BO(O)
        self.BP = BP(P)
        self.NC = NC
        self.NP = NP

    def start(self):
        for i in range(self.NC):
            self.cliente = Cliente(self.BO, self.BP)
            self.cliente.start()
        for i in range(self.NP):
            self.pizzaiolo = Pizzaiolo(self.BO, self.BP)
            self.pizzaiolo.start()

dimBO = 10
dimBP = 10
NumClienti = 5
NumPizzaioli = 3
Da_Toto = Pizzeria(dimBO, dimBP, NumClienti, NumPizzaioli)
Da_Toto.start()