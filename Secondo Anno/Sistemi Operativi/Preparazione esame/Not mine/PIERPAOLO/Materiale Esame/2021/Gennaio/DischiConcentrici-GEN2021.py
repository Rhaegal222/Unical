from threading import Thread,Lock,RLock,Condition
from random import random,randint
from time import sleep

debug = True

#
# Stampa sincronizzata
#
plock = Lock()
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


class DischiConcentrici():
    
    def __init__(self,size : int):
        #
        # Lock interno per la gestione della struttura dati
        #
        self.lock = RLock()
        self.waitCondition = Condition(self.lock)
        #
        # Tiene traccia della corrispondenza In e Out
        #
        self.shiftAttuale = 0
        #
        # I due array interni
        #
        self.In = [1] * size
        self.Out = [1] * size
        self.size = size
        
    #
    # Data in input una posizione in In, restituisce la posizione omologa in Out
    #
    def _om(self,i : int):
        with self.lock:
            dprint("I:%d" % i)
            return (i + self.shiftAttuale) % self.size

    #
    # Esempio, con len(In) = len(Out) = 10:
    #   shiftAttuale = 0, dunque _om(i) = i
    # 
    #  Corrispondenza tra In e Out:
    #
    #   In: 0 1 2 3 4 5 6 7 8 9
    #  Out: 0 1 2 3 4 5 6 7 8 9
    # 
    #  Dopo aver invocato shift(2) ==> shiftAttuale = 2, _om(i) = (i+2) % 10
    #
    #  Corrispondenza tra In e Out:
    #
    #   In: 0 1 2 3 4 5 6 7 8 9
    #  Out: 2 3 4 5 6 7 8 9 0 1 
    #

    def shift(self, m : int):
        with self.lock:
            self.shiftAttuale += m

    def set(self, i : int, v : int, d : int):
        with self.lock:
            if d == 0:
                self.Out[self._om(i)] = v
            else:
                self.In[i] = v
            if self.In[i] == self.Out[self._om(i)]:
                self.In[i] = 0
                self.Out[self._om(i)] = 0
            elif v != 0:
                self.waitCondition.notifyAll()

    def get(self, i : int, d : int):
        with self.lock:
            while (d == 0 and self.Out[self._om(i)] == 0) or (d == 1 and self.In[i] == 0):
                dprint("In attesa")
                self.waitCondition.wait()
            dprint("Risvegliato")
            if d == 0:
                return self.Out[self._om(i)]
            elif d == 1:
                return self.In[i]
    
class ManipolatoreDischi(Thread):

    def __init__(self, d : DischiConcentrici):
        super().__init__()
        self.iterazioni = 1000
        self.d = d

    def run(self):
        while(self.iterazioni > 0):
            self.iterazioni -= 1
            r = random()
            i = randint(0,self.d.size-1)
            v = randint(0,10)
            d = randint(0,1)
            if r < 0.5:
                sprint("get(%d,%d) = %d" % (i,d,self.d.get(i,d)))
            else:
                sprint("set(%d,%d,%d)" % (i,v,d))
                self.d.set(i,v,d)
            if r < 0.1:
                self.d.shift(i)
            sleep(random()/100)


D = DischiConcentrici(10)
for i in range(0,100):
    ManipolatoreDischi(D).start()
