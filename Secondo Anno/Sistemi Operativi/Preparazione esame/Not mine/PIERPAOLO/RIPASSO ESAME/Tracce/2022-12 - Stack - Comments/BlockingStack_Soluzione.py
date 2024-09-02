from threading import RLock,Condition, Thread
import random
import time

class BlockingStack:
    
    def __init__(self,size):
        self.size = size 
        self.elementi = [] 
        self.lock = RLock()
        self.conditionTuttoPieno = Condition(self.lock)
        self.conditionTuttoVuoto = Condition(self.lock)
        self.FIFO = False
        
    def __find(self,t):
        try:
            if self.elementi.index(t) >= 0:
                return True
        except(ValueError):
            return False
    
    def put(self,t):
        with self.lock:
            while len(self.elementi) == self.size:
                self.conditionTuttoPieno.wait()
            self.conditionTuttoVuoto.notify_all()
            self.elementi.append(t)
    
    def take(self,t=None):
        with self.lock:
            if t == None:
                if(self.FIFO == True):
                    while len(self.elementi) == 0:
                        self.conditionTuttoVuoto.wait()
                    if len(self.elementi) == self.size:
                        self.conditionTuttoPieno.notify()
                    return self.elementi.pop(0) # take as FIFO
                else:
                    while len(self.elementi) == 0:
                        self.conditionTuttoVuoto.wait()
                    if len(self.elementi) == self.size:
                        self.conditionTuttoPieno.notify()
                    return self.elementi.pop() # take as LIFO
            else:
                while not self.__find(t):
                    self.conditionTuttoVuoto.wait()
                if len(self.elementi) == self.size:
                    self.conditionTuttoPieno.notify()
                self.elementi.remove(t)    
                return t     
    
    def flush(self):
        with self.lock:
            self.elementi.clear()
    
    def putN(self, L : list): 
        if(self.FIFO):
            #rendi il metodo FIFO
            pass
        else:
            with self.lock:
                if(len(self.elementi)+len(L) <= self.size):
                    for i in L:
                        self.elementi.append(i)
                    self.conditionTuttoVuoto.notify_all()
                else:
                    self.conditionTuttoPieno.wait()

    def setFIFO(self, onOFF : bool):
        self.FIFO = onOFF

    
            
    

class Consumer(Thread): 
    
    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(random.random()*2)
            print(f"Estratto elemento {self.queue.take()}")
            


class Producer(Thread):

    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self): 
        while True:
            time.sleep(random.random() * 2)
            self.queue.put(self.name)
            
#  Main
#
buffer = BlockingStack(10)

producers = [Producer(buffer) for x in range(5)]
consumers = [Consumer(buffer) for x in range(3)]

for p in producers:
    p.start()

for c in consumers:
    c.start()
    
