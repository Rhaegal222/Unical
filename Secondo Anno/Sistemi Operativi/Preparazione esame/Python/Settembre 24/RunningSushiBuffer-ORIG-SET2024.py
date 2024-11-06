#!/usr/bin/env python

from threading import RLock, Condition, Thread
from time import sleep
import random

debug = True

#
# Stampa sincronizzata
#
plock = RLock()
def sprint(s):
    with plock:
        print(s)
#
# Stampa solo in debug mode
#
def dprint(s):
    with plock:
        if debug:
            print(s)

class RunningSushiBuffer:
    
    def __init__(self, dim):
        self.theBuffer = [None] * dim
        #
        # All'inizio la posizione 0 corrisponde proprio con la posizione 0 del buffer
        #
        self.zeroPosition = 0
        self.dim = dim
        self.lock = RLock()
        self.condition = Condition(self.lock)

    #
    # Questo metodo serve a virtualizzare gli indici del buffer circolare
    # Il valore della variabile self.zeroPosition ci dice quale elemento di self.theBuffer
    # va considerato come elemento 0
    #
    def __getRealPosition(self,i : int):
        return (i + self.zeroPosition) % self.dim    

    def get(self, pos : int):
        with self.lock:
            if pos <= 0 or pos >= self.dim:
                raise ValueError("Posizione non valida per una operazione di get")
            while self.theBuffer[self.__getRealPosition(pos)] == None:
                self.condition.wait()
            palluzza = self.theBuffer[self.__getRealPosition(pos)]
            self.theBuffer[self.__getRealPosition(pos)] = None
            return palluzza

    def put(self, t):
        with self.lock:
            while self.theBuffer[self.__getRealPosition(0)] != None:
                self.condition.wait()
            self.theBuffer[self.__getRealPosition(0)] = t

    def shift(self, j = 1):
        with self.lock:            
            # 
            #  uso zeroPosition per spostare la posizione 0 solo virtualmente, 
            #  anziche' dover ricopiare degli elementi
            # 
            self.zeroPosition = (self.zeroPosition + j) % self.dim
            # 
            #    E' solo grazie a uno shift che puo' crearsi la condizione per svegliare un thread
            #    in attesa, che potrebbe rispettivamente essere in attesa su put() o su get()
            # 
            self.condition.notify_all()

    #
    #  Implementazione di putList
    #
    def __checkFreePositions(self,n):
        for i in range(0,n):
            if self.theBuffer[self.__getRealPosition(i)] != None:
                return False
        return True

    def putList(self,L):
        with self.lock:
            while(not self.__checkFreePositions(len(L))):
                self.condition.wait()
            for elem in L:
                self.put(elem)
                self.shift()

    #
    # Implementazione di getList
    #
    def __rawPut(self,T,i):
        self.theBuffer[self.__getRealPosition(i)] = T

    def __attendi_shift(self,t,i):
        while self.theBuffer[self.__getRealPosition(i)] == t:
            self.condition.wait()

    def getList(self,N,t,i):
        with self.lock:
            retList = []
            elemDaPrendere = N
            while elemDaPrendere > 0:
                T = self.get(i)
                if T != t:
                    retList.append(T)
                    elemDaPrendere -= 1
                else:
                    # Questo item non mi piace, lo rimetto al suo posto e aspetto che il nastro scorra
                    self.__rawPut(T,i)
                    self.__attendi_shift(t,i)
            return retList


#
# Questo thread Ã¨ usato per fare scorrere periodicamente il nastro trasportatore
#
class NastroRotante(Thread):
    
    def __init__(self, d : RunningSushiBuffer):
        super().__init__()
        self.iterazioni = 10000
        self.d = d

    def run(self):
        while(self.iterazioni > 0):
            sleep(0.1)
            self.iterazioni -= 1
            self.d.shift()
            
class Cuoco(Thread):
    
    piatti = [ "*", ";", "^", "%", "!", "@" ]

    def __init__(self, d : RunningSushiBuffer):
        super().__init__()
        self.iterazioni = 1000
        self.d = d

    def run(self):
        while(self.iterazioni > 0):
            sleep(0.5 * random.random())
            self.iterazioni -= 1
            randPiatto = random.choice(self.piatti)
            self.d.put(randPiatto)
            dprint ( f"Il cuoco {self.ident} ha cucinato un ottimo <{randPiatto}>")
            randQuantita = random.randint(2,5)
            self.d.putList([randPiatto] * randQuantita)
            dprint ( f"Il cuoco {self.ident} ha cucinato {randQuantita} porzioni di <{randPiatto}>")
        dprint ( f"Il cuoco {self.ident} ha finito il suo turno e va via")

class Cliente(Thread):
    
    def __init__(self, d : RunningSushiBuffer, pos : int):
        super().__init__()
        self.quantitaCheVoglioMangiare = random.randint(1,20)
        self.d = d
        self.pos = pos

    def run(self):
        while(self.quantitaCheVoglioMangiare > 0):
            sleep(5 * random.random())
            self.quantitaCheVoglioMangiare -= 1
            dprint ( f"Il cliente {self.ident} aspetta cibo")
            dprint ( f"Il cliente {self.ident} mangia con gusto del <{self.d.get(self.pos)}>")
        dprint ( f"Il cliente {self.ident} ha la pancia piena e va via")

class GruppoClienti(Thread):

    def __init__(self, d : RunningSushiBuffer, pos : int, numClienti : int):
        super().__init__()
        self.numClienti = numClienti
        self.quantitaCheVogliamoMangiare = random.randint(1,20)
        self.cosaCheNonVogliamoMangiare = random.choice(Cuoco.piatti)
        self.d = d
        self.pos = pos

    def run(self):
        while(self.quantitaCheVogliamoMangiare > 0):
            sleep(5 * random.random())
            self.quantitaCheVogliamoMangiare -= self.numClienti
            dprint ( f"Il gruppo clienti {self.ident} aspetta cibo")
            dprint ( f"Il gruppo clienti {self.ident} mangia con gusto dei <{self.d.getList(self.numClienti,self.cosaCheNonVogliamoMangiare,self.pos)}>")

size = 20
D = RunningSushiBuffer(size)
NastroRotante(D).start()
for i in range(0,2):
    Cuoco(D).start()
for i in range(1,10):
    Cliente(D,i).start()
for i in range(10,20):
    GruppoClienti(D,i,random.randint(2,5)).start()